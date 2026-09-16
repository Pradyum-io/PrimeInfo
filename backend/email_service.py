import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from backend.config import (
    SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, SMTP_USE_TLS, NOTIFICATION_EMAIL
)

logger = logging.getLogger("backend.email")

def send_enquiry_notification(enquiry_data):
    """
    Send an email notification for a new contact form submission via SMTP.
    Returns True if sent, False otherwise. Does not throw exceptions.
    """
    if not SMTP_HOST or not SMTP_USER or not SMTP_PASSWORD:
        logger.warning(
            "SMTP is not configured (SMTP_HOST/USER/PASSWORD missing). Email notification skipped for ID %s.",
            enquiry_data.get("id")
        )
        return False

    recipient = NOTIFICATION_EMAIL or "Sadika.siddiqui55@gmail.com"
    subject = f"New Project Inquiry from {enquiry_data['name']}"
    if enquiry_data.get("company"):
        subject += f" ({enquiry_data['company']})"

    plain_body = f"""New Contact Form Submission received on PrimeCoreInfo:

Name: {enquiry_data['name']}
Work Email: {enquiry_data['work_email']}
Company: {enquiry_data.get('company') or '—'}
Phone: {enquiry_data.get('phone') or '—'}
Service Interested: {enquiry_data.get('service') or '—'}

Message:
----------------------------------------
{enquiry_data['message']}
----------------------------------------

Submitted at: {enquiry_data.get('created_at', 'N/A')}
Submission ID: {enquiry_data.get('id', 'N/A')}
"""

    html_body = f"""<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; color: #1e293b; background-color: #f8fafc; padding: 24px; margin: 0;">
  <div style="max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
    <h2 style="color: #0878c9; margin-top: 0; border-bottom: 2px solid #35d6e8; padding-bottom: 12px;">New Project Inquiry</h2>
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 24px; font-size: 15px;">
      <tr><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; font-weight: bold; width: 140px; color: #475569;">Name:</td><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; color: #0f172a;">{enquiry_data['name']}</td></tr>
      <tr><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; font-weight: bold; color: #475569;">Work Email:</td><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7;"><a href="mailto:{enquiry_data['work_email']}" style="color: #159fe8; text-decoration: none;">{enquiry_data['work_email']}</a></td></tr>
      <tr><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; font-weight: bold; color: #475569;">Company:</td><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; color: #0f172a;">{enquiry_data.get('company') or '—'}</td></tr>
      <tr><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; font-weight: bold; color: #475569;">Phone:</td><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; color: #0f172a;">{enquiry_data.get('phone') or '—'}</td></tr>
      <tr><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; font-weight: bold; color: #475569;">Service Interested:</td><td style="padding: 10px 0; border-bottom: 1px solid #edf2f7; color: #0f172a;">{enquiry_data.get('service') or '—'}</td></tr>
    </table>
    <h3 style="color: #0b2942; margin-bottom: 8px;">Message Content</h3>
    <div style="background: #f1f5f9; padding: 16px; border-radius: 8px; white-space: pre-wrap; font-size: 14px; line-height: 1.6; color: #334155; border-left: 4px solid #35d6e8;">{enquiry_data['message']}</div>
    <p style="font-size: 12px; color: #94a3b8; margin-top: 24px; text-align: right;">Submitted at: {enquiry_data.get('created_at', 'N/A')} &bull; Submission ID #{enquiry_data.get('id', 'N/A')}</p>
  </div>
</body>
</html>
"""

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = recipient
    msg["Reply-To"] = enquiry_data["work_email"]

    msg.attach(MIMEText(plain_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        if SMTP_USE_TLS:
            server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=10)

        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, [recipient], msg.as_string())
        server.quit()
        logger.info("Notification email sent for submission ID %s.", enquiry_data.get("id"))
        return True
    except Exception as err:
        logger.error("Failed to send notification email: %s", err)
        return False
