from django.urls import path
from driver.views import driver_register, update_driver_profile, CheckVerifications

urlpatterns = [
    # path('event/<uuid:event_id>/assign/<uuid:driver_id>/', AssignDriver, name='assign-driver'),
    # path('event/<uuid:event_id>/unassign/<uuid:driver_id>/', UnassignDriver, name='unassign-driver'),
    path('register/', driver_register, name='register_driver'),
    path('<str:driver_uuid>/update-profile/', update_driver_profile, name='update_driver_profile'),
    path('<str:email>/check-verifications/', CheckVerifications.as_view(), name='CheckVerifications'),
]