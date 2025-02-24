from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Event
from driver.models import Driver
from .utils import generate_otp, send_email_otp, verify_email

class DriverRegisterView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not verify_email(email):
            return Response({"error": "Invalid or undeliverable email address"}, status=status.HTTP_400_BAD_REQUEST)

        email_otp = generate_otp()
        print(email_otp)  # Remove in production

        # Store email and OTP in session
        request.session['userregister'] = {
            'email': email,
            'email_otp': email_otp,
        }

        send_email_otp(email, email_otp)

        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
    
class DriverRegisterVerifyOTPView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        email_otp = data.get('otp')  # Match frontend's key

        session_data = request.session.get('userregister')

        if not session_data:
            return Response({"error": "Session expired or no OTP found"}, status=status.HTTP_400_BAD_REQUEST)

        if email != session_data.get('email'):
            return Response({"error": "Email mismatch"}, status=status.HTTP_400_BAD_REQUEST)

        if email_otp == session_data.get('email_otp'):
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
    
class AssignDriverView(APIView):
    def post(self, request, event_id, driver_id):
        event = get_object_or_404(Event, id=event_id)
        driver = get_object_or_404(Driver, id=driver_id)
        event.drivers.add(driver)
        return Response({"message": "Driver assigned successfully"}, status=status.HTTP_200_OK)

class UnassignDriverView(APIView):
    def post(self, request, event_id, driver_id):
        event = get_object_or_404(Event, id=event_id)
        driver = get_object_or_404(Driver, id=driver_id)
        event.drivers.remove(driver)
        return Response({"message": "Driver unassigned successfully"}, status=status.HTTP_200_OK)