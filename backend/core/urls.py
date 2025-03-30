from django.urls import path
from .views import user_events, ToggleEventLikeView


urlpatterns = [
    path('events/', user_events, name='events'),
    path("events/<uuid:event_id>/like/", ToggleEventLikeView.as_view(), name="toggle-event-like"),
]