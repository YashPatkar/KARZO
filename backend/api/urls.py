from django.urls import path
from core.views import EventView

urlpatterns = [
    path('event/', EventView.as_view())
]