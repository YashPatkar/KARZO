from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from core.models import Event
from .serializers import EventSerializer
from .models import Event, EventLike

@api_view(['GET'])
def user_events(request):
    '''Send Events to frontend'''
    try:
        events = Event.objects.all()  # Query all events
        serialized_events = EventSerializer(events, many=True)  # Serialize the queryset
        return Response(serialized_events.data, status=status.HTTP_200_OK)  # Return serialized data
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class ToggleEventLikeView(APIView):
    def post(self, request, event_id):
        email = request.data.get("email")  # Get email from frontend

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        event = get_object_or_404(Event, id=event_id)

        like, created = EventLike.objects.get_or_create(event=event, email=email)

        if created:
            liked = True  # New like added
        else:
            like.delete()  # Unlike
            liked = False

        return Response({
            "liked": liked,
            "like_count": event.total_likes()
        }, status=status.HTTP_200_OK)