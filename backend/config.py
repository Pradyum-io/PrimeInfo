import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

def load_env():
    """Load environment variables from .env file if present."""
    if ENV_FILE.exists():
        try:
            with open(ENV_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, val = line.split("=", 1)
                        key = key.strip()
                        val = val.strip().strip("'\"")
                        if key and key not in os.environ:
                            os.environ[key] = val
        except Exception as e:
            print(f"Warning: Could not read .env file: {e}")

load_env()

class ConfigError(RuntimeError):
    """Raised when the configuration is unsafe for the selected environment."""

# Environment: "development" (default) or "production"
APP_ENV = os.environ.get("APP_ENV", "development").strip().lower()
IS_PRODUCTION = APP_ENV == "production"

# Server Settings
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", 8000))

# CORS: comma-separated list of allowed origins.
# Development defaults to "*". Production requires an explicit list (no "*").
REQUIRED_PRODUCTION_ORIGIN = "https://primecoreinfo.com"
_cors_raw = os.environ.get("CORS_ORIGINS", "").strip()

if IS_PRODUCTION:
    if not _cors_raw:
        raise ConfigError(
            "CORS_ORIGINS must be set in production (e.g. %s)." % REQUIRED_PRODUCTION_ORIGIN
        )
    CORS_ALLOWED_ORIGINS = {o.strip().rstrip("/") for o in _cors_raw.split(",") if o.strip()}
    if "*" in CORS_ALLOWED_ORIGINS:
        raise ConfigError("CORS_ORIGINS must not contain '*' in production.")
    CORS_ALLOWED_ORIGINS.add(REQUIRED_PRODUCTION_ORIGIN)
else:
    CORS_ALLOWED_ORIGINS = {
        o.strip().rstrip("/") for o in (_cors_raw or "*").split(",") if o.strip()
    }

# Serve static website files from this process? Off in production by default
# (the static site is hosted separately, e.g. on GitHub Pages).
SERVE_STATIC = os.environ.get("SERVE_STATIC", "false" if IS_PRODUCTION else "true").lower() in ("true", "1", "yes")

# Number of trusted reverse proxies in front of this server. 0 = use the direct
# socket address and ignore X-Forwarded-For entirely.
TRUSTED_PROXY_COUNT = int(os.environ.get("TRUSTED_PROXY_COUNT", 0))

# Database Settings. Relative paths resolve against the project root.
_db_raw = os.environ.get("DATABASE_PATH", "").strip()
if IS_PRODUCTION:
    if not _db_raw or not os.path.isabs(_db_raw):
        raise ConfigError(
            "DATABASE_PATH must be set to an absolute path on a persistent disk in production."
        )
    _db_dir = Path(_db_raw).parent
    if not _db_dir.is_dir() or not os.access(_db_dir, os.W_OK):
        raise ConfigError("DATABASE_PATH directory %s does not exist or is not writable." % _db_dir)
    DATABASE_PATH = _db_raw
else:
    _db_path = Path(_db_raw) if _db_raw else Path("enquiries.db")
    DATABASE_PATH = str(_db_path if _db_path.is_absolute() else BASE_DIR / _db_path)

# Email Settings
NOTIFICATION_EMAIL = os.environ.get("NOTIFICATION_EMAIL", "connect@primecoreinfo.com")
SMTP_HOST = os.environ.get("SMTP_HOST", "")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
SMTP_USE_TLS = os.environ.get("SMTP_USE_TLS", "true").lower() in ("true", "1", "yes")

# Anti-Spam & Rate Limiting Settings
RATE_LIMIT_MAX_REQUESTS = int(os.environ.get("RATE_LIMIT_MAX_REQUESTS", 5))
RATE_LIMIT_WINDOW_SECONDS = int(os.environ.get("RATE_LIMIT_WINDOW_SECONDS", 600))
