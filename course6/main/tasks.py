import smtplib
from email.mime.text import MIMEText
from django.utils import timezone
from .models import Mailing, Attempt

def send_mail(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.example.com') as server:
            server.login('your_email@example.com', 'your_password')
            server.sendmail('your_email@example.com', [to_email], msg.as_string())
        return 'success', 'Email sent successfully'
    except Exception as e:
        return 'failure', str(e)

def run_mailing():
    now = timezone.now()
    mailings = Mailing.objects.filter(first_send_time__lte=now, status='created')
    for mailing in mailings:
        for client in mailing.clients.all():
            status, response = send_mail(mailing.message.subject, mailing.message.body, client.email)
            Attempt.objects.create(mailing=mailing, status=status, response=response)
        mailing.status = 'completed'
        mailing.save()
