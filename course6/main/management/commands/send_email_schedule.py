from django.core.management.base import BaseCommand
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Command(BaseCommand):
    help = 'Sending email command'

    def handle(self, *args, **options):
        from_email = "your_email@gmail.com"
        to_email = "recipient_email@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Subject of the email"

        body = "Body of the email"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, "your_password")
        server.send_message(msg)
        server.quit()
