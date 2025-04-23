from django.conf import settings
from django.core.mail import send_mail
import uuid

import requests
from .models import RegistrationToken
from random import randint

def is_email_valid(email):
    try:
        url = "https://emailvalidation.abstractapi.com/v1/"
        params = {
            "api_key": settings.ABSTRACTAPI_EMAIL_VERIFICATION_KEY,
            "email": email
        }
        response = requests.get(url, params=params)
        data = response.json()

        return data.get("is_valid_format", {}).get("value", False) and data.get("is_smtp_valid", False)
    except Exception as e:
        return False
    
def generate_otp():
    return randint(100000, 999999)

def send_email(email):
    try:

        """Generate a unique registration link and send it via email"""
        token = str(uuid.uuid4())  # Generate a unique token
        print(email, token)
        # Save token to the database
        RegistrationToken.objects.update_or_create(email=email, defaults={"token": token})
        print('Generated token:', token)
        registration_link = f"{settings.FRONTEND_URL}/PRegisterCardExtendedView?token={token}"

        subject = "KARZO Registration Link."
        message = f"Click the link below to complete your registration:\n{registration_link}"
        sender = settings.EMAIL_HOST_USER
        recipients = [email]

        response = send_mail(subject, message, sender, recipients)
        print("Email Response:", response)
        return response
    except Exception as e:
        print("Error sending email:", str(e))
        return False

def send_email_otp(email, otp):
    subject = "KARZO Email OTP"
    message = f"Your email OTP is {otp} for KARZO. It is valid for 5 minutes. Do not share this with anyone."
    sender = settings.EMAIL_HOST_USER
    recipients = [email]

    response = send_mail(subject, message, sender, recipients)
    print("Email Response:", response)
    return response