# app/utilities/email.py

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.config import SENDGRID_API_KEY, FROM_EMAIL

def send_email(to: str, subject: str, body: str) -> dict:
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to,
        subject=subject,
        plain_text_content=body
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return {
            "status": "sent",
            "to": to,
            "subject": subject,
            "http_status": response.status_code
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
