from django.urls import path, include

urlpatterns = [
    path('driver/', include('driver.urls')),  # Include driver app URLs
    path('passenger/', include('passenger.urls')),  # Include passenger app URLs
    path('core/', include('core.urls')),  # Include core app URLs
]