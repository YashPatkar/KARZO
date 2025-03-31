from django.urls import path
from driver.views import (
    check_otp,
    check_user,
    driver_register,
    event_submit,
    resend_otp,
    validate_token,
)

urlpatterns = [
        path("validate-token/", validate_token, name="validate_token"),
        path("register/", driver_register, name="register_driver"),
        path("check-user/", check_user.as_view(), name="check_user"),
        path("check-otp/", check_otp, name="check_otp"),
        path("register/", driver_register, name="register_driver"),
        path("<str:email>/resend-otp/", resend_otp, name="resend_otp"),
        path("submit-event/", event_submit, name="submit-event"),
]
