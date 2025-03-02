from django.urls import path
from core.views import EventView

core_patterns = [
    path('event/', EventView.as_view()),
]
