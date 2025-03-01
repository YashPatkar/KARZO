from django.urls import path
# Core
from core.views import EventView
# Driver
from driver.views import AssignDriver, UnassignDriver, DriverRegister, DriverRegisterVerifyOTP
# -----------------------------------------------------------------------------

# Core URLs for common functionality (e.g., events)
core_patterns = [
    path('event/', EventView.as_view()),
]

# Driver-specific URLs
driver_patterns = [
    path('event/<uuid:event_id>/assign/<uuid:driver_id>/', AssignDriver, name='assign-driver'),
    path('event/<uuid:event_id>/unassign/<uuid:driver_id>/', UnassignDriver, name='unassign-driver'),
    path('driver/driver-register/', DriverRegister, name='driver-register'),
    path('driver/verify-email-otp/', DriverRegisterVerifyOTP, name='driver-register-verify-otp'),
]

# Passenger-specific URLs
# passenger_patterns = [
# ]

# Combine all patterns
urlpatterns = core_patterns + driver_patterns #+ passenger_patterns
