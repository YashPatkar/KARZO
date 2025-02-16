from django.urls import path
# Core
from core.views import EventView
# Driver
from driver.views import AssignDriverView, UnassignDriverView
# -----------------------------------------------------------------------------

# Core URLs for common functionality (e.g., events)
core_patterns = [
    path('event/', EventView.as_view()),
]

# Driver-specific URLs
driver_patterns = [
    path('event/<uuid:event_id>/assign/<uuid:driver_id>/', AssignDriverView.as_view(), name='assign-driver'),
    path('event/<uuid:event_id>/unassign/<uuid:driver_id>/', UnassignDriverView.as_view(), name='unassign-driver'),
]

# Passenger-specific URLs
# passenger_patterns = [
# ]

# Combine all patterns
urlpatterns = core_patterns + driver_patterns #+ passenger_patterns
