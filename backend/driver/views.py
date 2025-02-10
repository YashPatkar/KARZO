from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Event
from driver.models import Driver

class AssignDriverView(APIView):
    def post(self, request, event_id, driver_id):
        event = get_object_or_404(Event, id=event_id)
        driver = get_object_or_404(Driver, id=driver_id)
        event.drivers.add(driver)  # Add driver to the event
        return Response({"message": "Driver assigned successfully"}, status=status.HTTP_200_OK)

class UnassignDriverView(APIView):
    def post(self, request, event_id, driver_id):
        event = get_object_or_404(Event, id=event_id)
        driver = get_object_or_404(Driver, id=driver_id)
        event.drivers.remove(driver)  # Remove driver from the event
        return Response({"message": "Driver unassigned successfully"}, status=status.HTTP_200_OK)
