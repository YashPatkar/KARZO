from random import randint
import requests
from django.conf import settings
from django.core.mail import send_mail

def generate_otp():
    return randint(100000, 999999)

def verify_email(email):
    if not email:
        return False
    """Check if an email is real and valid using AbstractAPI."""
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={settings.ABSTRACTAPI_EMAIL_VERIFICATION_KEY}&email={email}"
    response = requests.get(url).json()
    
    return response.get("deliverability") == "DELIVERABLE"

def verify_phone(phone):
    if not phone:
        return False
    """Check if a phone number is valid and active using AbstractAPI."""
    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={settings.ABSTRACTAPI_PHONE_VERIFICATION_KEY}&phone={phone}"
    response = requests.get(url).json()
    
    return response.get("valid") is True

def send_email_otp(email, otp):
    subject = "KARZO Email OTP"
    message = f"Your email OTP is {otp} for KARZO. It is valid for 5 minutes. Do not share this with anyone."
    sender = settings.EMAIL_HOST_USER
    recipients = [email]

    response = send_mail(subject, message, sender, recipients)
    print("Email Response:", response)  # Debugging
    return response