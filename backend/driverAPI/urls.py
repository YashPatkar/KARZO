from django.urls import include, path
from core import views
import rest_framework

urlpatterns = [
    path('/event/', views.event.as_view()),    
]