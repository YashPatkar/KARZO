from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EventSerializer
from .models import Event

class EventStoreDataView(APIView):
    # POST request to create a new event
    def post(self, request):
        data = request.data
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)
    
class EventGetDataView(APIView):
    def post(self, request):
        try:
            data = Event.objects.all()
            if data:
                return Response(data)
        except:
            return Response(status=400)