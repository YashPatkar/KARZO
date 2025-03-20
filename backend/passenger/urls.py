from django.urls import path
from .views import (
    check_otp,
    validate_token,
    passenger_register,
    check_user,
    event_submit,
)

urlpatterns = [
    path("validate-token/", validate_token, name="validate_token"),
    path("register/", passenger_register, name="register_passenger"),
    path("check-user/", check_user.as_view(), name="check_user"),
    path("check-otp/", check_otp, name="check_otp"),
    path("submit-event/", event_submit, name="submit_event"),
]
