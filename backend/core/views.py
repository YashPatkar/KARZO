from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import EventSerializer
from core.models import Event
# Create your views here.

class Event(APIView): # api/event/
    def get(self, request):
        
        try:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        data = request.data
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)