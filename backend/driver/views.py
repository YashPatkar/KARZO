from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Event
from driver.models import Driver
from .utils import generate_otp, send_email_otp, verify_email
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt



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