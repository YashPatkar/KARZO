from datetime import datetime, timedelta, timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class DriverRegistrationToken(models.Model):
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

class DriverUser(models.Model):
    """
    Model to store driver-specific user data.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="driver")  # Link to Django's User model
    email = models.EmailField(unique=True)  # Email of the driver
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the driver was registered

    def __str__(self):
        return f"Driver: {self.email}"

class PersonalDetails(models.Model):
    """
    Model to store personal details of the driver.
    """
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    driver = models.OneToOneField(DriverUser, on_delete=models.CASCADE, related_name="personal_details")
    full_name = models.CharField(max_length=255, default="Unknown")
    age = models.PositiveIntegerField(validators=[MinValueValidator(14), MaxValueValidator(120)], default=18)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    phone_number = models.CharField(max_length=15, default="0000000000")
    address = models.TextField(default="Not provided")
    profile_photo = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Personal Details for {self.driver.email}"

class VehicleDetails(models.Model):
    """
    Model to store vehicle details of the driver.
    """
    driver = models.OneToOneField(DriverUser, on_delete=models.CASCADE, related_name="vehicle_details")
    vehicle_number = models.CharField(max_length=20, unique=True, default="UNKNOWN")
    vehicle_manufacturer = models.CharField(max_length=50, default="Unknown Manufacturer")
    vehicle_type = models.CharField(max_length=50, default="Unknown Type")
    vehicle_model = models.CharField(max_length=50, default="Unknown Model")
    vehicle_color = models.CharField(max_length=20, default="Unknown Color")
    registration_number = models.CharField(max_length=50, unique=True, default="UNKNOWN")
    vehicle_registration_date = models.DateField(null=True, blank=True)  # Allow null values

    def __str__(self):
        return f"Vehicle: {self.vehicle_number} - {self.driver.email}"
