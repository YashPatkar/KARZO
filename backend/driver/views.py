from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from core.models import Event
from driver.models import PersonalDetails
from .utils import generate_otp, send_email_otp
from django.contrib.auth.models import User
from .serializers import PersonalDetailsSerializer, VehicleDetailsSerializer
from .models import DriverUser, PersonalDetails
from uuid import UUID
from django.core.cache import cache
from django.conf import settings

# @api_view(['GET'])
# def AssignDriver(self, request, event_id, driver_id):
#     event = get_object_or_404(Event, id=event_id)
#     driver = get_object_or_404(Driver, id=driver_id)
#     event.drivers.add(driver)
#     return Response({"message": "Driver assigned successfully"}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def UnassignDriver(self, request, event_id, driver_id):
#     event = get_object_or_404(Event, id=event_id)
#     driver = get_object_or_404(Driver, id=driver_id)
#     event.drivers.remove(driver)
#     return Response({"message": "Driver unassigned successfully"}, status=status.HTTP_200_OK)

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
                # Generate OTP
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
        '''API endpoint to verify the OTP'''
        try:
            driver = DriverUser.objects.filter(email=email).first()
            if not driver:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            otp = cache.get(email)
            if not otp:
                return Response({"message": "OTP expired or not found"}, status=status.HTTP_400_BAD_REQUEST)

            user_otp = request.data.get('otp')
            if not user_otp:
                return Response({"error": "OTP is required"}, status=status.HTTP_400_BAD_REQUEST)

            if str(user_otp) == str(otp):  # Compare as strings
                cache.delete(email)  # Remove OTP from cache after successful verification
                return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        