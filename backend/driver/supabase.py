import requests
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def send_otp(phone_number):
    url = f"{SUPABASE_URL}/auth/v1/otp"
    headers = {
        "apikey": SUPABASE_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "phone": phone_number,
        "channel": "sms"  # or "whatsapp" if enabled
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
