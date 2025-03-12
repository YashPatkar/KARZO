from django.urls import path
from driver.views import driver_register, user_submitted_event, update_driver_profile, resend_otp, CheckVerifications, send_driver_data

urlpatterns = [
    # path('event/<uuid:event_id>/assign/<uuid:driver_id>/', AssignDriver, name='assign-driver'),
    # path('event/<uuid:event_id>/unassign/<uuid:driver_id>/', UnassignDriver, name='unassign-driver'),
    path('register/', driver_register, name='register_driver'),
    path('<str:driver_uuid>/update-profile/', update_driver_profile, name='update_driver_profile'),
    path('<str:email>/check-verifications/', CheckVerifications.as_view(), name='CheckVerifications'),
    path('<str:email>/resend-otp/', resend_otp, name='resend_otp'),
    path('<str:email>/driver-data/', send_driver_data, name='send_driver_data'),
    path('submit-event/', user_submitted_event, name='submit-event'),
]