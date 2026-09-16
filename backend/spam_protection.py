import time
import logging
from collections import defaultdict
from backend.config import RATE_LIMIT_MAX_REQUESTS, RATE_LIMIT_WINDOW_SECONDS

logger = logging.getLogger("backend.spam_protection")

# In-memory IP submission history
_ip_history = defaultdict(list)
_last_submission = {}

def is_rate_limited(ip_address):
    """Check if the requesting IP address has exceeded the rate limit."""
    if not ip_address:
        return False

    now = time.time()
    cutoff = now - RATE_LIMIT_WINDOW_SECONDS

    # Filter out requests older than window
    recent_requests = [t for t in _ip_history[ip_address] if t > cutoff]
    _ip_history[ip_address] = recent_requests

    if len(recent_requests) >= RATE_LIMIT_MAX_REQUESTS:
        logger.warning("Rate limit exceeded for IP %s (%d requests in %ds).",
                       ip_address, len(recent_requests), RATE_LIMIT_WINDOW_SECONDS)
        return True

    recent_requests.append(now)
    return False

def is_rapid_duplicate(ip_address, email):
    """Check if same IP/email submitted within 5 seconds."""
    key = f"{ip_address}:{email}"
    now = time.time()
    last_time = _last_submission.get(key, 0)
    if now - last_time < 5.0:
        logger.warning("Rapid duplicate submission blocked for key %s.", key)
        return True
    _last_submission[key] = now
    return False

def check_honeypot(data):
    """Check if honeypot field is filled by spam bot."""
    if not isinstance(data, dict):
        return False
    # If any common honeypot field is populated, flag as spam
    for field in ["_website", "honeypot", "confirm_email_address", "hp"]:
        if data.get(field):
            logger.warning("Honeypot field '%s' triggered.", field)
            return True
    return False
