from django.urls import path
from .views import (
    PassengerProfile,
    cancel_event_booking,
    check_otp,
    get_event_bookings,
    passenger_feedback,
    validate_token,
    passenger_register,
    check_user,
    event_submit,
    book_event,
    resend_otp
)

urlpatterns = [
    path("validate-token/", validate_token, name="validate_token"),
    path("register/", passenger_register, name="register_passenger"),
    path("check-user/", check_user.as_view(), name="check_user"),
    path("check-otp/", check_otp, name="check_otp"),
    path('resend-otp/<str:email>/', resend_otp, name='resend_otp'),
    path("submit-event/", event_submit, name="submit_event"),
    path('book-event/', book_event, name='book_event'),
    path('passenger-profile/', PassengerProfile.as_view(), name='passenger_profile'),
    path('feedback/', passenger_feedback, name='passenger_feedback'),
    path('bookings/', get_event_bookings),
    path('bookings/<int:request_id>/', cancel_event_booking),
]
