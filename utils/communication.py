import os
from typing import List, Optional
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENGRID_EMAIL_SENDER = os.getenv("SENGRID_EMAIL_SENDER")

sengridEmailSender = SendGridAPIClient(SENDGRID_API_KEY)


def send_email(
    to_emails: List[str],
    subject: str,
    plain_text_content: Optional[str] = "",
):
    message = Mail(
        from_email=SENGRID_EMAIL_SENDER,
        to_emails=to_emails,
        subject=subject,
        plain_text_content=plain_text_content,
    )
    sengridEmailSender.send(message)
