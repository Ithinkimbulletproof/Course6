from django.core.management.base import BaseCommand
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time


class Command(BaseCommand):
    help = 'Sending email on schedule'

    def send_email(self):
        from_email = "your_email@gmail.com"
        to_email = "recipient_email@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Тема письма"

        body = "Текст сообщения"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, "your_password")
        server.send_message(msg)
        server.quit()

    def handle(self, *args, **options):
        schedule.every().day.at("10:00").do(self.send_email)

        while True:
            schedule.run_pending()
            time.sleep(1)
