from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import User
from driver.serializers import EventRequestSerializer
from .models import DriverFeedback, DriverUser, PersonalDetails, DriverRegistrationToken, VehicleDetails
from django.core.cache import cache
import re
from driver.utils import send_email_driver as se, generate_otp_driver as go, send_email_otp_driver as seotp
from core.models import EventRequest, otpData, Event
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
        print("New OTP: ", new_otp)
        cache.set(email, new_otp, timeout=300)  # Store OTP for 5 minutes
        print("Cached OTP: ", cache.get(email))
        print("Email: ", email)
        email_response = seotp(email, new_otp)
        print("Email responsee: ", email_response)

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

@api_view(["GET", "POST"])
def toggle_working(request):
    """
    GET: Return current working status
    POST: Update working status with explicit value
    """
    email = request.data.get("email") if request.method == "POST" else request.query_params.get("email")

    if not email:
        return Response({"error":
         "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        driver_user = DriverUser.objects.filter(email=email).first()
        if not driver_user:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            return Response({
                "working": driver_user.is_working,
                "message": "Current working status retrieved"
            }, status=status.HTTP_200_OK)

        elif request.method == "POST":
            new_status = request.data.get("working")
            if new_status is None:
                return Response({"error": "Working status is required"}, status=status.HTTP_400_BAD_REQUEST)

            driver_user.is_working = new_status
            driver_user.save()
            
            return Response({
                "working": driver_user.is_working,
                "message": "Working status updated successfully"
            }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "error": f"Unexpected error: {str(e)}",
            "working": driver_user.is_working if 'driver_user' in locals() else None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_event_requests_for_driver(request):
    try:
        email = request.query_params.get('email')
        if not email:
            return Response({"error": "Driver email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            driver = DriverUser.objects.get(email=email)
        except DriverUser.DoesNotExist:
            return Response({"error": "Driver not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get all PENDING event requests for this driver
        event_requests = EventRequest.objects.filter(driver=driver, status='PENDING').order_by('-created_at')
        serializer = EventRequestSerializer(event_requests, many=True)
        data = serializer.data

        # Collect all unique event_ids
        event_ids = [item.get("event_id") for item in data]
        print("Event IDs:", event_ids)

        # Query event details for these event_ids
        event_map = {
            str(event.id): {
                "event_name": event.event_name,
                "event_location": event.location,
            }
            for event in Event.objects.filter(id__in=event_ids)
        }

        # Merge event_name and event_location into each item
        for item in data:
            event_id = item.get("event_id")
            if event_id in event_map:
                item["event_name"] = event_map[event_id]["event_name"]
                item["event_location"] = event_map[event_id]["event_location"]

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        print("Error fetching driver event requests:", e)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ApproveRequestView(APIView):
    def post(self, request):
        try:
            data = request.data
            print('Received data:', data)
            
            event_uuid = data.get("event_id")
            if not event_uuid:
                return Response({"error": "event_id is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            event = get_object_or_404(EventRequest, event_id=event_uuid)
            print('Found event:', event)
                        
            return Response({
                "message": "Event request approved",
                "event": {
                    "event_id": event.event_id,
                    "passenger_name": event.passenger_name,
                    "pickup_location": event.pickup_location,
                    "event_name": event.event_name,
                    "status": event.status
                }
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            print('Error:', str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class DriverProfile(APIView):
    def get(self, request):
        try:
            driver_email = request.query_params.get("email")  # Changed from request.data to query_params
            if not driver_email:
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            driver = DriverUser.objects.filter(email=driver_email).first()
            if not driver:
                return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

            # Construct custom response
            personal = getattr(driver, 'personal_details', None)
            response_data = {
                "email": driver.email,
                "name": personal.full_name if personal else "",
                "phone": personal.phone_number if personal else "",
                "address": personal.address if personal else "",
                "profile_photo": personal.profile_photo if personal else ""
            }

            return Response({"data": response_data}, status=status.HTTP_200_OK)

        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            driver_email = request.data.get("email")
            if not driver_email:
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

            driver = DriverUser.objects.filter(email=driver_email).first()
            if not driver:
                return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

            # Update personal details
            personal_details = driver.personal_details
            if personal_details:
                personal_details.full_name = request.data.get("name", personal_details.full_name)
                personal_details.profile_photo = request.data.get("profile_photo", personal_details.profile_photo)
                personal_details.save()

            return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def driver_feedback(request):
    """
    API endpoint to submit driver feedback.
    """
    try:
        data = request.data
        driver_email = data.get("email")
        feedback_text = data.get("message")
        print(data)
        if not driver_email or not feedback_text:
            return Response({"error": "Email and feedback are required"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Get driver object
        driver = DriverUser.objects.filter(email=driver_email).first()
        print('driver:', driver)
        if not driver:
            return Response({"error": "driver not found"}, status=status.HTTP_404_NOT_FOUND)

        # ✅ Create feedback object
        DriverFeedback.objects.create(
            driver=driver,
            feedback_text=feedback_text
        )
        print(DriverFeedback)

        return Response({"message": "Feedback submitted successfully"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)