from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Event

# # class EventView(APIView): # api/event/
# #     # giving all event data to frontend
# #     def get(self, request):
# #         try:
# #             events = Event.objects.all()
# #             serializer = EventSerializer(events, many=True)
# #             return Response(serializer.data, status=status.HTTP_200_OK)
# #         except Exception as e:
# #             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# #     # saving event data from frontend
# #     def post(self, request):
# #         data = request.data
# #         serializer = EventSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(status=status.HTTP_201_CREATED)
# #         return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_events(request):
    '''giving all event data to frontend'''
    try:
        events = Event.objects.all()
        return Response(events, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
