from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.views import APIView
import re
from .utils import send_email
from .models import RegistrationToken
from django.contrib.auth.models import User
from .models import PassengerUser
from .utils import generate_otp, send_email_otp
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import RegistrationToken, PassengerUser, PersonalDetails
from .utils import send_email
from core.models import otpData
from core.serializers import EventSerializer


@api_view(["POST"])
def passenger_register(request):
    """
    API endpoint to register a new Passenger.
    """
    data = request.data
    email = data.get("email")
    token = data.get("token")
    profile_photo_url = data.get("profile_photo")  # Get the profile photo URL
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
                    return Response(
                        status=status.HTTP_200_OK
                    )
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
    
@api_view(['POST'])
def book_event(request):
    try:
        data = request.data
        print('data:', data)
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        print("Error: ", e)
        return Response(status=status.HTTP_304_NOT_MODIFIED)