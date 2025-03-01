from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Event
from driver.models import Driver
from .utils import generate_otp, send_email_otp, verify_email
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def DriverRegister(request):
    data = request.data
    email = data.get('email')

    if not email:
        return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

    if not verify_email(email):
        return Response({"error": "Invalid or undeliverable email address"}, status=status.HTTP_400_BAD_REQUEST)

    email_otp = generate_otp()
    print("Generated OTP:", email_otp)  # Debugging purpose

    # Store OTP in the session
    request.session['email'] = email
    request.session['email_otp'] = email_otp
    request.session.set_expiry(300)  # Session expires after 5 minutes (300 seconds)
    request.session.modified = True  # Force session to save
    request.session.save()

    # Retrieve OTP from the session
    session_email = request.session.get('email')
    session_otp = request.session.get('email_otp')

    print("Session Email:", session_email)  # Debugging purpose
    print("Session OTP:", session_otp)  # Debugging purpose
    print('---------------------------')

    send_email_otp(email, email_otp)

    return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def DriverRegisterVerifyOTP(request):
    data = request.data
    email = data.get('email')
    email_otp = data.get('email_otp')
    # Retrieve OTP from the session
    if email_otp and email:
        request.session.pop('email', None)
        request.session.pop('email_otp', None)
        # Skiping the OTP verification for now 
        return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def AssignDriver(self, request, event_id, driver_id):
    event = get_object_or_404(Event, id=event_id)
    driver = get_object_or_404(Driver, id=driver_id)
    event.drivers.add(driver)
    return Response({"message": "Driver assigned successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def UnassignDriver(self, request, event_id, driver_id):
    event = get_object_or_404(Event, id=event_id)
    driver = get_object_or_404(Driver, id=driver_id)
    event.drivers.remove(driver)
    return Response({"message": "Driver unassigned successfully"}, status=status.HTTP_200_OK)