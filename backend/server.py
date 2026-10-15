import json
import logging
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import os

from backend.config import (
    BASE_DIR, HOST, PORT, IS_PRODUCTION, CORS_ALLOWED_ORIGINS, SERVE_STATIC, TRUSTED_PROXY_COUNT
)
from backend.database import init_db, save_enquiry
from backend.validation import validate_contact_form
from backend.email_service import send_enquiry_notification
from backend.spam_protection import is_rate_limited, is_rapid_duplicate, check_honeypot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
)
logger = logging.getLogger("backend.server")

# Only these file types are ever served as static files (local development only).
PUBLIC_STATIC_EXTENSIONS = {
    ".html", ".css", ".js", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif",
    ".ico", ".mp4", ".webm", ".woff", ".woff2", ".xml",
}
BLOCKED_TOP_LEVEL_DIRS = {"backend", "__pycache__", "node_modules"}

class ContactAPIHandler(SimpleHTTPRequestHandler):
    """HTTP Request Handler providing /api/contact endpoint & (dev-only) static file server."""

    timeout = 15  # seconds; drops stalled connections

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def _allowed_origin(self):
        """Return the Access-Control-Allow-Origin value for this request, or None."""
        if "*" in CORS_ALLOWED_ORIGINS:
            return "*"
        origin = (self.headers.get("Origin") or "").rstrip("/")
        return origin if origin in CORS_ALLOWED_ORIGINS else None

    def _set_cors_headers(self):
        """Set Cross-Origin Resource Sharing (CORS) headers for allowed origins only."""
        allowed = self._allowed_origin()
        if allowed:
            self.send_header("Access-Control-Allow-Origin", allowed)
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Accept")
        self.send_header("Vary", "Origin")

    def _client_ip(self):
        """Direct socket address, unless trusted proxies are configured."""
        direct = self.client_address[0]
        if TRUSTED_PROXY_COUNT <= 0:
            return direct
        hops = [h.strip() for h in (self.headers.get("X-Forwarded-For") or "").split(",") if h.strip()]
        # Each trusted proxy appends the address it saw; count from the right.
        if len(hops) >= TRUSTED_PROXY_COUNT:
            return hops[-TRUSTED_PROXY_COUNT]
        return direct

    def _send_json_response(self, status_code, payload):
        """Helper to send a JSON HTTP response."""
        response_data = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self._set_cors_headers()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(response_data)

    def _static_allowed(self):
        """Allowlist check for static requests (dev only)."""
        if not SERVE_STATIC:
            return False
        try:
            target = Path(self.translate_path(self.path)).resolve()
            rel = target.relative_to(Path(BASE_DIR).resolve())
        except (ValueError, OSError):
            return False
        parts = rel.parts
        if any(p.startswith(".") for p in parts):
            return False
        if parts and parts[0] in BLOCKED_TOP_LEVEL_DIRS:
            return False
        if target.is_dir():
            return (target / "index.html").is_file()
        return target.suffix.lower() in PUBLIC_STATIC_EXTENSIONS and target.is_file()

    def list_directory(self, path):
        self.send_error(404, "Not found")
        return None

    def do_HEAD(self):
        if self.path.startswith("/api/") or not self._static_allowed():
            self.send_error(404, "Not found")
            return
        super().do_HEAD()

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        if self.path.startswith("/api/"):
            if not self._allowed_origin():
                self._send_json_response(403, {"success": False, "error": "Origin not allowed."})
                return
            self.send_response(204)
            self._set_cors_headers()
            self.end_headers()
        else:
            self.send_error(404, "Not found")

    def do_GET(self):
        """Handle GET requests for API health check or (dev-only) static files."""
        parsed_path = urllib.parse.urlparse(self.path).path.rstrip("/")

        if parsed_path == "/api/contact" or parsed_path == "/api/health":
            self._send_json_response(200, {
                "status": "online",
                "service": "PrimeCoreInfo Contact API"
            })
            return

        if parsed_path.startswith("/api") or not self._static_allowed():
            self._send_json_response(404, {"success": False, "error": "Not found."})
            return

        super().do_GET()

    def do_POST(self):
        """Handle POST requests for contact form submission."""
        parsed_path = urllib.parse.urlparse(self.path).path.rstrip("/")
        
        if parsed_path != "/api/contact":
            self._send_json_response(404, {"success": False, "error": "Endpoint not found."})
            return

        # Browsers always send Origin on cross-origin POSTs; reject unlisted ones.
        # (Requests with no Origin header, e.g. curl, are still subject to all other checks.)
        if self.headers.get("Origin") and not self._allowed_origin():
            self._send_json_response(403, {"success": False, "error": "Origin not allowed."})
            return

        # Client address: direct socket peer unless trusted proxies are configured
        client_ip = self._client_ip()

        # Check Rate Limiting
        if is_rate_limited(client_ip):
            self._send_json_response(429, {
                "success": False,
                "error": "Too many requests. Please wait a few minutes before submitting again."
            })
            return

        # Read Request Body with Size Limit (50 KB max)
        try:
            content_length = int(self.headers.get("Content-Length", 0))
        except ValueError:
            content_length = 0

        if content_length > 50000:
            self._send_json_response(413, {"success": False, "error": "Payload size too large."})
            return

        body_bytes = self.rfile.read(content_length)
        content_type = self.headers.get("Content-Type", "")

        # Parse payload
        data = {}
        try:
            if "application/json" in content_type:
                data = json.loads(body_bytes.decode("utf-8") or "{}")
            elif "application/x-www-form-urlencoded" in content_type:
                parsed = urllib.parse.parse_qs(body_bytes.decode("utf-8"))
                data = {k: v[0] for k, v in parsed.items()}
            else:
                # Try fallback JSON parsing
                data = json.loads(body_bytes.decode("utf-8") or "{}")
        except Exception as e:
            logger.warning("Failed to parse request body: %s", e)
            self._send_json_response(400, {"success": False, "error": "Invalid request format."})
            return

        # Honeypot Check
        if check_honeypot(data):
            # Silently pretend success to mislead spam bots
            self._send_json_response(200, {
                "success": True,
                "message": "Thank you. Your inquiry has been submitted."
            })
            return

        # Validate Fields
        is_valid, errors, cleaned_data = validate_contact_form(data)
        if not is_valid:
            self._send_json_response(400, {
                "success": False,
                "error": "Validation failed.",
                "details": errors
            })
            return

        # Rapid Duplicate Submission Check
        if is_rapid_duplicate(client_ip, cleaned_data["work_email"]):
            self._send_json_response(429, {
                "success": False,
                "error": "Duplicate submission detected. Please wait a moment."
            })
            return

        # Save to Database
        try:
            saved_record = save_enquiry(
                name=cleaned_data["name"],
                work_email=cleaned_data["work_email"],
                company=cleaned_data["company"],
                phone=cleaned_data["phone"],
                service=cleaned_data["service"],
                message=cleaned_data["message"]
            )
        except Exception as e:
            logger.error("Failed to save enquiry to database: %s", e)
            self._send_json_response(500, {
                "success": False,
                "error": "An internal database error occurred. Please try again later."
            })
            return

        # Send Email Notification in Background Thread
        Thread(target=send_enquiry_notification, args=(saved_record,), daemon=True).start()

        # Return Success JSON Response
        self._send_json_response(201, {
            "success": True,
            "message": "Thank you! Your inquiry has been received.",
            "id": saved_record["id"]
        })

def run_server(host=HOST, port=PORT):
    """Initialize DB and run HTTP Server."""
    init_db()
    server_address = (host, port)
    httpd = ThreadingHTTPServer(server_address, ContactAPIHandler)
    logger.info("PrimeCoreInfo Backend Server (%s) listening on %s:%d, static=%s",
                "production" if IS_PRODUCTION else "development", host, port, SERVE_STATIC)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server stopping...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
