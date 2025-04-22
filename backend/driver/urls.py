from django.urls import path
from driver.views import (
    ApproveRequestView,
    DriverProfile,
    check_otp,
    check_user,
    driver_register,
    event_submit,
    get_event_requests_for_driver,
    resend_otp,
    validate_token,
    toggle_working,
)

urlpatterns = [
        path("validate-token/", validate_token, name="validate_token"),
        path("register/", driver_register, name="register_driver"),
        path("check-user/", check_user.as_view(), name="check_user"),
        path("check-otp/", check_otp, name="check_otp"),
        path("register/", driver_register, name="register_driver"),
        path('resend-otp/<str:email>/', resend_otp, name='resend_otp'),
        path("submit-event/", event_submit, name="submit-event"),
        path("toggle-working/", toggle_working, name="toggle-working"),
        path('event-requests/', get_event_requests_for_driver, name='driver_event_requests'),
        path('approve-request/', ApproveRequestView.as_view(), name='approve_request'),
        path('driver-profile/', DriverProfile.as_view(), name='driver_profile'),
]
