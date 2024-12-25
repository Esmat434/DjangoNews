from django.conf import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(content,email,subject='For activate your account click on this link'):
    message = MIMEMultipart()
    message['from'] = settings.EMAIL_HOST_USER
    message['to'] = email
    message['subject'] = 'Welcome to MBC NEWS '
    link = f'<p>{subject}: <a href="http://127.0.0.1:8000/{content}">{content}</a></p>'
    message.attach(MIMEText(link,'html'))
    with smtplib.SMTP(host=settings.EMAIL_HOST,port = settings.EMAIL_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user=settings.EMAIL_HOST_USER,password=settings.EMAIL_HOST_PASSWORD)
        smtp.send_message(message)
        print("Email Successfully Sended!")