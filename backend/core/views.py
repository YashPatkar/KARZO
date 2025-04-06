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
        email = request.data.get("email")

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        event = get_object_or_404(Event, id=event_id)

        try:
            like = EventLike.objects.get(event=event, email=email)
            like.delete()
            liked = False
        except EventLike.DoesNotExist:
            EventLike.objects.create(event=event, email=email)
            liked = True

        like_count = EventLike.objects.filter(event=event).count()

        return Response({
            "liked": liked,
            "like_count": like_count
        }, status=status.HTTP_200_OK)

class EventLikeCountView(APIView):
    def get(self, request, event_id):
        try:
            event = get_object_or_404(Event, id=event_id)
            like_count = event.total_likes()
            return Response({"like_count": like_count}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)