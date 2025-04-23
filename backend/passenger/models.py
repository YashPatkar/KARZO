from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class RegistrationToken(models.Model):
    """
    Model to store registration tokens for passenger sign-up.
    """
    email = models.EmailField(unique=True)  # Email associated with the token
    token = models.CharField(max_length=255, unique=True)  # Unique token for registration
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the token was created
    expires_at = models.DateTimeField()  # Expiration time for the token

    def save(self, *args, **kwargs):
        """
        Override the save method to set expires_at to 5 hours from the current time.
        """
        if not self.expires_at:  # Set expires_at only if it's not already set
            self.expires_at = datetime.now(timezone.utc) + timedelta(hours=5)
        super().save(*args, **kwargs)

    def is_expired(self):
        """
        Check if the token has expired.
        """
        return datetime.now(timezone.utc) > self.expires_at

    def __str__(self):
        return f"Token for {self.email} (Expires: {self.expires_at})"

class PassengerUser(models.Model):
    """
    Model to store passenger-specific user data.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="passenger")  # Link to Django's User model
    email = models.EmailField(unique=True)  # Email of the passenger
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the passenger was registered

    def __str__(self):
        return f"Passenger: {self.email}"

class PersonalDetails(models.Model):
    """
    Model to store personal details of the passenger.
    """
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    passenger = models.OneToOneField(PassengerUser, on_delete=models.CASCADE, related_name="personal_details")  # Link to PassengerUser
    full_name = models.CharField(max_length=255)  # Full name of the passenger
    age = models.PositiveIntegerField(validators=[MinValueValidator(14), MaxValueValidator(120)])  # Age of the passenger
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")  # Gender of the passenger
    phone_number = models.CharField(max_length=15)  # Phone number of the passenger
    address = models.TextField()  # Address of the passenger
    profile_photo = models.URLField(blank=True, null=True)  # **NEW: Profile photo URL field**

    def __str__(self):
        return f"Personal Details for {self.passenger.email}"
    
class PassengerFeedback(models.Model):
    """
    Model to store feedback from passengers.
    """
    passenger = models.ForeignKey(PassengerUser, on_delete=models.CASCADE, related_name="feedback")  # Link to PassengerUser
    feedback_text = models.TextField()  # Feedback text from the passenger
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the feedback was submitted

    def __str__(self):
        return f"Feedback from {self.passenger.email} on {self.created_at}"
    