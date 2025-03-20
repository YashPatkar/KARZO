from django.conf import settings
from django.core.mail import send_mail
import uuid
from .models import RegistrationToken
from random import randint

def generate_otp():
    return randint(100000, 999999)

def send_email(email):
    """Generate a unique registration link and send it via email"""
    token = str(uuid.uuid4())  # Generate a unique token

    # Save token to the database
    RegistrationToken.objects.update_or_create(email=email, defaults={"token": token})

    registration_link = f"{settings.FRONTEND_URL}/PRegisterCardExtendedView?token={token}"

    subject = "KARZO Registration Link."
    message = f"Click the link below to complete your registration:\n{registration_link}"
    sender = settings.EMAIL_HOST_USER
    recipients = [email]

    response = send_mail(subject, message, sender, recipients)
    return response


def send_email_otp(email, otp):
    subject = "KARZO Email OTP"
    message = f"Your email OTP is {otp} for KARZO. It is valid for 5 minutes. Do not share this with anyone."
    sender = settings.EMAIL_HOST_USER
    recipients = [email]

    response = send_mail(subject, message, sender, recipients)
    print("Email Response:", response)
    return response