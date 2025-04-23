from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.views import APIView
import re

from test import is_email_valid
from .models import PassengerFeedback, RegistrationToken
from django.contrib.auth.models import User
from .models import PassengerUser
from .utils import generate_otp, send_email_otp, send_email
from rest_framework import status
from .models import RegistrationToken, PassengerUser, PersonalDetails
from core.models import Event, EventRequest, otpData
from core.serializers import EventSerializer
from driver.models import DriverUser
from geopy.distance import geodesic
from django.core.cache import cache
from driver.utils import generate_otp_driver as go, send_email_otp_driver as seotp

@api_view(["POST"])
def passenger_register(request):
    """
    API endpoint to register a new Passenger.
    """
    data = request.data
    email = data.get("email")
    token = data.get("token")
    profile_photo_url = data.get("profile_photo")  # Get the profile photo URL
    if not is_email_valid(email):
        return Response(
            {"error": "Invalid email format"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    print(data)
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
        registration = RegistrationToken.objects.get(token=token, email=email)
        if not registration:
            return Response(
                {"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST,
            )
    except RegistrationToken.DoesNotExist:
        return Response(
            {"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        # Check if a user with this email already exists
        user, created = User.objects.get_or_create(
            email=email, defaults={"username": email}
        )

        # Check if the user is already registered as a passenger
        if PassengerUser.objects.filter(user=user).exists():
            return Response(
                {"error": "User is already registered as a passenger"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create PassengerUser
        passenger = PassengerUser.objects.create(user=user, email=email)

        # Create PersonalDetails with profile photo URL
        PersonalDetails.objects.create(
            passenger=passenger,
            full_name=data.get("name", ""),
            age=data.get("age"),
            gender=data.get("gender", "male"),
            phone_number=data.get("phone", ""),
            address=data.get("address", ""),
            profile_photo=profile_photo_url,  # Save the profile photo URL
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

@api_view(['POST'])
def resend_otp(request, email):
    """API endpoint to resend OTP to the user"""
    try:
        email = str(email).lower()
        passenger = PassengerUser.objects.filter(email=email).first() 

        if not passenger:
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

@api_view(["POST"])
def validate_token(request):
    """
    Validate the token provided.
    """
    token = request.data.get("token")
    print("Token is: ", token)
    if not token:
        print("Token is missing")
        return Response(
            {"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        registration = RegistrationToken.objects.filter(token=token).first()
        print("Registration token exists: ", registration)
        print('======')
        if not registration:
            print("Token does not exist")
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST,
            )
        if registration:
            return Response({"email": registration.email}, status=status.HTTP_200_OK)
        
    except RegistrationToken.DoesNotExist:
        print('------')
        print("Token does not exist")
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST,)


class check_user(APIView):
    def get(self, request):
        """Sending passenger data to Frontend."""
        try:
            email = request.GET.get("email")
            print("email is: ", email)
            if not email:
                return Response(
                    {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST,
                )

            # Fetch PassengerUser object
            passenger_user = PassengerUser.objects.filter(email=email).first()
            if not passenger_user:
                return Response(
                    {"error": "Passenger not found"}, status=status.HTTP_404_NOT_FOUND
                )

            # Fetch PersonalDetails for the passenger
            personal_details = PersonalDetails.objects.filter(
                passenger=passenger_user
            ).first()
            print("personal_details: ", personal_details)
            if not personal_details:
                return Response(
                    {"error": "Personal details not found for this passenger"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            # Return the required data
            first_name = re.match(r"\S+", personal_details.full_name.strip()).group() if personal_details.full_name else ""
            return Response(
                {
                    "name": first_name,  # Get name
                    "email": passenger_user.email,  # Get email from PassengerUser
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
        Check if a user with the provided email exists.
        """
        email = request.data.get("email")
        if not email:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            if PassengerUser.objects.filter(email=email).exists():
                otp = generate_otp()
                if send_email_otp(email, otp):
                    # Save the OTP to the database
                    try:
                        otp_data = otpData(email=email, otp=otp)
                        otp_data.save()
                    except Exception as e:
                        return Response(
                            status=status.HTTP_302_FOUND,
                        )
                    response = Response(status=status.HTTP_200_OK)
                    response.set_cookie(
                        key='daily_auth',
                        value='true',
                        max_age=86400,  # 1 day
                        httponly=False,  # allow frontend to access it
                        samesite='Lax',
                        secure=False     # change to True if HTTPS
                    )
                    return response
                else:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                # Send registration link to the user
                registration_link = send_email(email)
                if registration_link:
                    return Response(status=status.HTTP_201_CREATED)
                return Response(
                    {"message": "User does not exist"},
                    status=status.HTTP_304_NOT_MODIFIED,
                )
        except Exception as e:
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
        return Response(status=status.HTTP_304_NOT_MODIFIED)
    try:
        otp_data = otpData.objects.get(email=email, otp=otp)
        if otp_data.is_expired():
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        return Response(status=status.HTTP_200_OK)
    except otpData.DoesNotExist:
        return Response(status=status.HTTP_304_NOT_MODIFIED)

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
    


# data: {'event_id': '1c32c2eb-4603-4330-aee0-b33ccd52c1cb', 'driver_preference': 'any', 'vehicle_preference': 'regular_bike', 'pickup_location': 'Fishermen Colony, G/N Ward, Zone 2, Mumbai, Maharashtra, 400016, India', 'latitude': 19.04708991834686, 'longitude': 72.84160345252239}

@api_view(['POST'])
def book_event(request):
    try:
        data = request.data
        print('data:', data)
        if not data:
            return Response({"error": "No data provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        pickup_location = (data.get("latitude"), data.get("longitude"))
        driver_preference = data.get("driver_preference", "any").lower()
        active_drivers = DriverUser.objects.filter(is_working=True)
        print("Active drivers:", active_drivers.count())
        print("Active drivers:", active_drivers)
        
        if driver_preference == "men":
            active_drivers = active_drivers.filter(personal_details__gender__iexact="male")
        elif driver_preference == "women":
            active_drivers = active_drivers.filter(personal_details__gender__iexact="female")
        
        passenger = PassengerUser.objects.get(email=data.get("passenger_email"))
        event = Event.objects.get(id=data.get("event_id"))
        
        nearby_drivers = []
        drivers_sent = 0
        
        for driver in active_drivers:
            print(drivers_sent)
            if drivers_sent >= 3:
                break  # stop once 3 drivers have been notified
            
            try:
                print("Driver email:", driver.email)
                driver_details = driver.personal_details
                
                # Ensure the driver's location exists and is valid
                if driver_details.latitude is None or driver_details.longitude is None:
                    print(f"Invalid location for driver {driver.email}. Skipping.")
                    continue
                
                driver_location = (driver_details.latitude, driver_details.longitude)
                distance = geodesic(pickup_location, driver_location).km
                print("Distance:", distance)
                
                if distance <= 5:
                    # Ensure the passenger is correctly passed in the EventRequest
                    event_request = EventRequest.objects.create(
                        event_id=event.id,
                        event_name=event.event_name,
                        email=event.email,
                        passenger_email=passenger.email,
                        passenger_name=passenger.personal_details.full_name,
                        driver=driver,
                        pickup_location=data.get("pickup_location"),
                        distance_km=round(distance, 2),
                        passenger=passenger  # Ensure this is added
                    )
                    
                    nearby_drivers.append({
                        "driver_email": driver.email,
                        "distance_km": round(distance, 2)
                    })
                    drivers_sent += 1
            except Exception as inner_e:
                print("Driver location missing or invalid:", inner_e)
                continue
        
        if nearby_drivers:
            return Response({
                "message": f"Requests sent to {drivers_sent} nearby drivers.",
                "drivers": nearby_drivers
            }, status=status.HTTP_201_CREATED)
        
        return Response({"message": "No suitable driver found nearby."}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        print("Error:", e)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PassengerProfile(APIView):
    def get(self, request):
        try:
            passenger_email = request.query_params.get("email")  # Changed from request.data to query_params
            if not passenger_email:
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            passenger = PassengerUser.objects.filter(email=passenger_email).first()
            if not passenger:
                return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

            # Construct custom response
            personal = getattr(passenger, 'personal_details', None)
            response_data = {
                "email": passenger.email,
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
            passenger_email = request.data.get("email")
            if not passenger_email:
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

            passenger = PassengerUser.objects.filter(email=passenger_email).first()
            if not passenger:
                return Response({"error": "Passenger not found"}, status=status.HTTP_404_NOT_FOUND)

            # Update personal details
            personal_details = passenger.personal_details
            if personal_details:
                personal_details.full_name = request.data.get("name", personal_details.full_name)
                print("Full name:", personal_details.full_name)
                personal_details.profile_photo = request.data.get("profile_photo", personal_details.profile_photo)
                print("Profile photo:", personal_details.profile_photo)
                personal_details.save()
                print("Personal details saved successfully")

            return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def passenger_feedback(request):
    """
    API endpoint to submit passenger feedback.
    """
    try:
        data = request.data
        passenger_email = data.get("email")
        feedback_text = data.get("message")

        if not passenger_email or not feedback_text:
            return Response({"error": "Email and feedback are required"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Get passenger object
        passenger = PassengerUser.objects.filter(email=passenger_email).first()
        if not passenger:
            return Response({"error": "Passenger not found"}, status=status.HTTP_404_NOT_FOUND)

        # ✅ Create feedback object
        PassengerFeedback.objects.create(
            passenger=passenger,
            feedback_text=feedback_text
        )

        return Response({"message": "Feedback submitted successfully"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_event_bookings(request):
    email = request.GET.get('email')
    if not email:
        return Response({"error": "Passenger email is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    passenger = PassengerUser.objects.filter(email=email).first()
    if not passenger:
        return Response({"error": "Passenger not found."}, status=status.HTTP_404_NOT_FOUND)

    bookings = EventRequest.objects.filter(passenger=passenger).order_by('-id')
    data = [
        {
            "id": booking.id,
            "event_name": booking.event_name,
            "pickup_location": booking.pickup_location,
            "driver_email": booking.driver.email if booking.driver else None,
            "distance_km": booking.distance_km,
        }
        for booking in bookings
    ]
    return Response({"bookings": data}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def cancel_event_booking(request, request_id):
    try:
        booking = EventRequest.objects.filter(id=request_id).first()
        if not booking:
            return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)

        booking.delete()
        return Response({"message": "Booking cancelled successfully."}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)