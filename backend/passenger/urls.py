from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('hello/', lambda request: HttpResponse(request, "Hello, World!"), name='hello'),
]