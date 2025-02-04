from django.urls import path
from core.views import Event

urlpatterns = [
    path('event/', Event.as_view())
]