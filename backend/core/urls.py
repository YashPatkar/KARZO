from django.urls import path
from django.http import HttpResponse as h
# from core.views import EventView

urlpatterns = [
    # path('event/', EventView.as_view()),
    path('event/', lambda request: h(request, 'Hello, World!')),
]