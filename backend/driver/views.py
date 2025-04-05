from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from driver.models import PersonalDetails
from django.contrib.auth.models import User
from .models import DriverUser, PersonalDetails, DriverRegistrationToken, VehicleDetails
from django.core.cache import cache
import re
from driver.utils import send_email_driver as se, generate_otp_driver as go, send_email_otp_driver as seotp
from core.models import otpData
from core.serializers import EventSerializer

@api_view(["POST"])
def driver_register(request):
    """
    API endpoint to register a new Driver.
    """
    data = request.data
    email = data.get("email")
    token = data.get("token")
    profile_photo_url = data.get("profile_photo")  # Get the profile photo URL
    print('data:', data)
    print("Email:", email)
    print("Token:", token)
    print("Profile Photo URL:", profile_photo_url)
    if not email or not token:
        return Response(
            {"error": "Email and token are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validate Token
    try:
        registration = DriverRegistrationToken.objects.get(token=token, email=email)
        if not registration:
            return Response(
                {"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST
            )
    except DriverRegistrationToken.DoesNotExist:
        return Response(
            {"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Check if a user with this email already exists
        user, created = User.objects.get_or_create(
            email=email, defaults={"username": email}
        )

        # Check if the user is already registered as a driver
        if DriverUser.objects.filter(user=user).exists():
            print('User is already registered as a driver', DriverUser.objects.filter(user=user))
            return Response(
                {"error": "User is already registered as a driver"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create DriverUser
        driver = DriverUser.objects.create(user=user, email=email)

        # Create PersonalDetails with profile photo URL
        PersonalDetails.objects.create(
            driver=driver,
            full_name=data.get("name", ""),
            age=data.get("age"),
            gender=data.get("gender", "male"),
            phone_number=data.get("phone", ""),
            address=data.get("address", ""),
            profile_photo=profile_photo_url,  # Save the profile photo URL
        )

        # Create VehicleDetails
        VehicleDetails.objects.create(
            driver=driver,
            vehicle_number=data.get("vehicle_number", ""),
            vehicle_manufacturer=data.get("vehicle_manufacturer", ""),
            vehicle_type=data.get("vehicle_type", ""),
            vehicle_model=data.get("vehicle_model", ""),
            vehicle_color=data.get("vehicle_color", ""),
            registration_number=data.get("registration_number", ""),
            vehicle_registration_date=data.get("vehicle_registration_date", ""),            
        )

        # Delete token after successful registration
        registration.delete()

        return Response(
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        print("Error:", str(e))
        return Response(
            {"error": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

class check_user(APIView):
    def get(self, request):
        """Sending Driver data to Frontend."""
        try:
            email = request.GET.get("email")
            print("email is: ", email)
            if not email:
                return Response(
                    {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
                )

            # Fetch DriverUser object
            driver_user = DriverUser.objects.filter(email=email).first()
            if not driver_user:
                return Response(
                    {"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND
                )

            # Fetch PersonalDetails for the driver
            personal_details = PersonalDetails.objects.filter(
                driver=driver_user
            ).first()
            print("personal_details: ", personal_details)
            if not personal_details:
                return Response(
                    {"error": "Personal details not found for this driver"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            # Return the required data
            first_name = re.match(r"\S+", personal_details.full_name.strip()).group() if personal_details.full_name else ""
            return Response(
                {
                    "name": first_name,  # Get name
                    "email": driver_user.email,
                    "profile_photo": personal_details.profile_photo,  # Get profile photo URL
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            print('---------------')
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_302_FOUND,
            )

    def post(self, request):
        """
        Check if a driver with the provided email exists.
        """
        email = request.data.get("email")
        if not email:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            if DriverUser.objects.filter(email=email).exists():
                otp = go()
                if seotp(email, otp):
                    # Save the OTP to the database
                    try:
                        otp_data = otpData(email=email, otp=otp)
                        otp_data.save()
                    except Exception as e:
                        return Response(
                            status=status.HTTP_302_FOUND,
                        )
                    return Response(
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                # Send registration link to the user
                print('-----------01', email, email)
                registration_link = se(email)
                if registration_link:
                    print('-----------1')
                    return Response(status=status.HTTP_201_CREATED)
                print('--------2')
                return Response(
                    {"message": "User does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print(e)
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_302_FOUND,
            )

@api_view(["POST"])
def check_otp(request):
    """
    Check if the OTP provided is valid.
    """
    email = request.data.get("email")
    otp = request.data.get("otp")
    if not email or not otp:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        otp_data = otpData.objects.get(email=email, otp=otp)
        if otp_data.is_expired():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
    except otpData.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def resend_otp(request, email):
    """API endpoint to resend OTP to the user"""
    try:
        email = str(email).lower()
        driver = DriverUser.objects.filter(email=email).first() 

        if not driver:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        new_otp = go()
        cache.set(email, new_otp, timeout=300)  # Store OTP for 5 minutes

        email_response = se(email, new_otp)

        if email_response == 1:
            return Response({"message": "OTP resent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def event_submit(request):
    try:
        data = request.data
        print('data:', data)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Error: ", e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def validate_token(request):
    """
    Validate the token provided.
    """
    token = request.data.get("token")
    print('token:', token)
    if not token:
        print('Token is required')
        return Response(
            {"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        registration = DriverRegistrationToken.objects.get(token=token)
        if not registration:
            return Response(
                {"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"email": registration.email}, status=status.HTTP_200_OK)
    except DriverRegistrationToken.DoesNotExist:
        print('Invalid tokennnnnnnn')
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
