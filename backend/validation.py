import re
import html

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def sanitize_text(text, max_len=2000):
    """Sanitize string inputs by stripping whitespace and escaping HTML."""
    if text is None:
        return ""
    cleaned = str(text).strip()
    escaped = html.escape(cleaned)
    return escaped[:max_len]

def validate_contact_form(data):
    """
    Validate contact form submission fields.
    Returns (is_valid, errors, cleaned_data).
    """
    if not isinstance(data, dict):
        return False, {"_all": "Invalid submission data payload."}, {}

    errors = {}

    # Extract fields
    name_raw = data.get("name") or ""
    email_raw = data.get("email") or data.get("work_email") or ""
    company_raw = data.get("company") or ""
    phone_raw = data.get("phone") or ""
    service_raw = data.get("service") or ""
    message_raw = data.get("message") or ""

    # Sanitize
    name = sanitize_text(name_raw, max_len=120)
    email = sanitize_text(email_raw, max_len=160)
    company = sanitize_text(company_raw, max_len=120)
    phone = sanitize_text(phone_raw, max_len=50)
    service = sanitize_text(service_raw, max_len=100)
    message = sanitize_text(message_raw, max_len=3000)

    # Name validation
    if not name:
        errors["name"] = "Name is required."
    elif len(name) < 2:
        errors["name"] = "Name must be at least 2 characters long."

    # Email validation
    if not email:
        errors["email"] = "Work email is required."
    elif not EMAIL_REGEX.match(email_raw.strip()):
        errors["email"] = "Please provide a valid work email address."

    # Message validation
    if not message:
        errors["message"] = "Message is required."
    elif len(message) < 5:
        errors["message"] = "Message must be at least 5 characters long."

    # Optional phone pattern check
    if phone:
        digits = re.sub(r"[^\d+]", "", phone)
        if len(digits) < 7:
            errors["phone"] = "Please enter a valid phone number."

    is_valid = len(errors) == 0
    cleaned_data = {
        "name": name,
        "work_email": email,
        "company": company,
        "phone": phone,
        "service": service,
        "message": message
    }

    return is_valid, errors, cleaned_data
