from django.db import models
import uuid
from driver.models import DriverUser
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    drivers = models.ManyToManyField(DriverUser, related_name='events', blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    driver_name = models.CharField(max_length=100)  # New field
    driver_email = models.EmailField()  # New field
    user_type = models.CharField(max_length=50, choices=[('driver', 'Driver'), ('passenger', 'Passenger')])  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.date}'
    
class otpData(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.email} - {self.otp}'
    
    def is_expired(self):
        return (timezone.now() - self.created_at).seconds > 300