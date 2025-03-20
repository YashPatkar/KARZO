from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from driver.models import PersonalDetails
from .utils import generate_otp, send_email_otp
from django.contrib.auth.models import User
from .serializers import PersonalDetailsSerializer, VehicleDetailsSerializer, EventSerializer
from .models import DriverUser, PersonalDetails
from uuid import UUID
from django.core.cache import cache

@api_view(['POST'])
def driver_register(request):
    """
    API endpoint to register a new driver.
    """
    data = request.data
    print('data:', data)
    
    driver_data = data.get('driver', {})
    print('driver_data:', driver_data)
    email = driver_data.get('email')
    if not email:
        return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

    # **Check if a user with the email already exists**
    user, created = User.objects.get_or_create(username=email, defaults={"email": email})
    print('user:', user)
    if not created and DriverUser.objects.filter(user=user).exists():
        return Response({"error": "Driver already registered with this email"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # **Create the DriverUser instance**
        driver = DriverUser.objects.create(user=user, email=email)
        print('driver:', driver)
        # Save Personal Details
        personal_details_data = data.get('personal_details', {})
        print('personal_details_data:', personal_details_data)
        personal_details_data['driver'] = driver.id  # ✅ Pass only the ID
        personal_details_serializer = PersonalDetailsSerializer(data=personal_details_data)
        print('personal_details_serializer:', personal_details_serializer)
        if not personal_details_serializer.is_valid():
            driver.delete()
            return Response(personal_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        personal_details_serializer.save()

        # Save Vehicle Details
        vehicle_details_data = data.get('vehicle_details', {})
        vehicle_details_data['driver'] = driver.id  # ✅ Pass only the ID
        vehicle_details_serializer = VehicleDetailsSerializer(data=vehicle_details_data)

        if not vehicle_details_serializer.is_valid():
            driver.delete()
            PersonalDetails.objects.filter(driver=driver).delete()
            return Response(vehicle_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        vehicle_details_serializer.save()

        # Return success response
        return Response(
            {
                'message': 'Driver registered successfully!',
                'driver_uuid': str(driver.id),
            },
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        driver.delete()
        return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PATCH'])
def update_driver_profile(request, driver_uuid):
    """
    API endpoint to update the profile of a driver.
    """
    try:
        driver_uuid = UUID(driver_uuid)
        print('driver_uuid:', driver_uuid)
        # Get the DriverUser instance first
        driver_user = DriverUser.objects.get(id=driver_uuid)
        print('driver_user:', driver_user)
        # Retrieve the related PersonalDetails instance
        driver = PersonalDetails.objects.get(driver=driver_user)
        print('driver:', driver)
    except (DriverUser.DoesNotExist, PersonalDetails.DoesNotExist):
        return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

    profile_photo_url = request.data.get('profile_photo_url')
    print('profile_photo_url:', profile_photo_url)
    if profile_photo_url:
        driver.profile_photo_url = profile_photo_url
        driver.save()
    print('User Registration Successful')
    return Response(
        {
            'message': 'Driver profile updated successfully!',
            'driver': PersonalDetailsSerializer(driver).data,  # Return correct data
        },
        status=status.HTTP_200_OK,
    )

class CheckVerifications(APIView):
    def get(self, request, email):
        '''API endpoint to check if a user is verified'''
        try:
            print('------------------')
            email = str(email).lower()
            driver = DriverUser.objects.filter(email=email).first()
            print(driver)

            if driver:  # Only verifying email
                otp = generate_otp()
                print(otp, email)
                # Store OTP temporarily (5 minutes expiry)
                cache.set(email, otp, timeout=300)

                # Send OTP via Django Email (Using utils.py function)
                email_response = send_email_otp(email, otp)
                print('email_response:', email_response)

                if email_response == 1:  # send_mail returns 1 if successful
                    return Response({"message": "OTP sent successfully to email"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"message": "User is not verified or does not exist"}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            print('asdasdasdasdsad')
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, email):
        '''API endpoint to send an OTP to the user's email'''
        try:
            email = str(email).lower()
            driver = DriverUser.objects.filter(email=email).first()
            if not driver:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            otp = generate_otp()
            cache.set(email, otp, timeout=300)  # Store OTP for 5 minutes

            # Send OTP via Django Email (Using utils.py function)
            email_response = send_email_otp(email, otp)
            if email_response == 1:  # send_mail returns 1 if successful
                return Response({"message": "OTP sent successfully to email"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def resend_otp(request, email):
    """API endpoint to resend OTP to the user"""
    try:
        email = str(email).lower()
        driver = DriverUser.objects.filter(email=email).first() 

        if not driver:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        new_otp = generate_otp()
        cache.set(email, new_otp, timeout=300)  # Store OTP for 5 minutes

        email_response = send_email_otp(email, new_otp)

        if email_response == 1:
            return Response({"message": "OTP resent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def send_driver_data(request, email):
    
    try:
        # Fetch driver using get_object_or_404
        print('email:', email)
        driver = get_object_or_404(DriverUser, email=email)

        # Fetch personal details securely using OneToOneField
        try:
            personal_details = PersonalDetails.objects.get(driver=driver)
        except PersonalDetails.DoesNotExist:
            return Response({"error": "Personal details not found"}, status=status.HTTP_404_NOT_FOUND)

        # Return all driver + personal details
        return Response(
            {
                'driver': {
                    'email': driver.email,
                    'name': personal_details.name,
                    'profile_photo_url': personal_details.profile_photo_url,
                }
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:

        print(e)
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
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Error2222222: ", e)
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)