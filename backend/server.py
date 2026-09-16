import json
import logging
import urllib.parse
from http.server import SimpleHTTPRequestHandler, HTTPServer
from threading import Thread
import os

from backend.config import HOST, PORT, CORS_ORIGINS
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

class ContactAPIHandler(SimpleHTTPRequestHandler):
    """HTTP Request Handler providing /api/contact endpoint & static file server."""

    def _set_cors_headers(self):
        """Set Cross-Origin Resource Sharing (CORS) headers."""
        self.send_header("Access-Control-Allow-Origin", CORS_ORIGINS)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Accept")

    def _send_json_response(self, status_code, payload):
        """Helper to send a JSON HTTP response."""
        response_data = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self._set_cors_headers()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_data)))
        self.end_headers()
        self.wfile.write(response_data)

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        if self.path.startswith("/api/"):
            self.send_response(204)
            self._set_cors_headers()
            self.end_headers()
        else:
            super().do_OPTIONS()

    def do_GET(self):
        """Handle GET requests for API health check or static files."""
        parsed_path = urllib.parse.urlparse(self.path).path.rstrip("/")
        
        if parsed_path == "/api/contact" or parsed_path == "/api/health":
            self._send_json_response(200, {
                "status": "online",
                "service": "PrimeCoreInfo Contact API",
                "version": "1.0.0"
            })
            return

        # Fallback to standard static file handling
        super().do_GET()

    def do_POST(self):
        """Handle POST requests for contact form submission."""
        parsed_path = urllib.parse.urlparse(self.path).path.rstrip("/")
        
        if parsed_path != "/api/contact":
            self._send_json_response(404, {"success": False, "error": "Endpoint not found."})
            return

        # Get client IP address
        client_ip = self.headers.get("X-Forwarded-For", self.client_address[0]).split(",")[0].strip()

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
    httpd = HTTPServer(server_address, ContactAPIHandler)
    logger.info("PrimeCoreInfo Backend Server running on http://%s:%d", host if host != "0.0.0.0" else "127.0.0.1", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server stopping...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
