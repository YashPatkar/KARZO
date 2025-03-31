from random import randint
import requests
from django.conf import settings
from django.core.mail import send_mail
import uuid
from .models import DriverRegistrationToken

def generate_otp_driver():
    return randint(100000, 999999)

def send_email_driver(email):
    """Generate a unique registration link and send it via email"""
    token = str(uuid.uuid4())  # Generate a unique token
    print(token)

    # Save token to the database
    DriverRegistrationToken.objects.update_or_create(email=email, defaults={"token": token})
    print('Generated token:', token)
    registration_link = f"{settings.FRONTEND_URL}/DRegisterCardExtendedView?token={token}"
    print('Registration link:', registration_link)

    subject = "KARZO Registration Link."
    message = f"Click the link below to complete your registration:\n{registration_link}"
    sender = settings.EMAIL_HOST_USER
    recipients = [email]

    print('Sending email to:', email)
    response = send_mail(subject, message, sender, recipients)
    return response


def send_email_otp_driver(email, otp):
    subject = "KARZO Email OTP"
    message = f"Your email OTP is {otp} for KARZO. It is valid for 5 minutes. Do not share this with anyone."
    sender = settings.EMAIL_HOST_USER
    recipients = [email]

    response = send_mail(subject, message, sender, recipients)
    print("Email Response:", response)
    return response
