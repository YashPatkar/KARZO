from django.urls import include, path
from core import views
import rest_framework

urlpatterns = [
    path('event/store-data/', views.EventStoreDataView.as_view()), 
    path('event/get-data/', views.EventGetDataView.as_view()),
]