from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Event
from driver.models import Driver, PersonalDetails
from .utils import generate_otp, send_email_otp, verify_email
from .serializers import DriverUserSerializer, PersonalDetailsSerializer, VehicleDetailsSerializer
from .models import DriverUser, PersonalDetails, VehicleDetails

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

@api_view(['POST'])
def driver_register(request):
    """
    API endpoint to register a new driver.
    """
    if request.method == 'POST':
        data = request.data

        # Validate and save DriverUser
        driver_data = data.get('driver', {})
        print('driver_data:', driver_data)
        driver_serializer = DriverUserSerializer(data=driver_data)
        if not driver_serializer.is_valid():
            return Response(driver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        driver = driver_serializer.save()

        # Validate and save PersonalDetails
        personal_details_data = data.get('personal_details', {})
        print('personal_details_data:', personal_details_data)
        personal_details_data['driver'] = driver.id  # Link to the DriverUser
        personal_details_serializer = PersonalDetailsSerializer(data=personal_details_data)
        if not personal_details_serializer.is_valid():
            driver.delete()  # Rollback DriverUser if PersonalDetails is invalid
            return Response(personal_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        personal_details_serializer.save()

        # Validate and save VehicleDetails
        vehicle_details_data = data.get('vehicle_details', {})
        print('vehicle_details_data:', vehicle_details_data)
        vehicle_details_data['driver'] = driver.id  # Link to the DriverUser
        vehicle_details_serializer = VehicleDetailsSerializer(data=vehicle_details_data)
        if not vehicle_details_serializer.is_valid():
            driver.delete()  # Rollback DriverUser and PersonalDetails if VehicleDetails is invalid
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

@api_view(['PATCH'])
def update_driver_profile(request, driver_uuid):
    """
    API endpoint to update the profile of a driver.
    """
    try:
        driver = PersonalDetails.objects.get(id=driver_uuid)
    except PersonalDetails.DoesNotExist:
        return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

    profile_photo_url = request.data.get('profile_photo_url')
    if profile_photo_url:
        driver.profile_photo_url = profile_photo_url
        driver.save()

    return Response(
        {
            'message': 'Driver profile updated successfully!',
            'driver': DriverUserSerializer(driver).data,
        },
        status=status.HTTP_200_OK,
    )