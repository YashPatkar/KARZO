from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()  # The person who created the event
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=300)
    description = models.TextField()
    user_type = models.CharField(max_length=50, choices=[('driver', 'Driver'), ('passenger', 'Passenger')])  
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return EventLike.objects.filter(event=self).count()

class EventLike(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="likes")
    email = models.EmailField()  # Storing likes based on email
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'email')  # Prevent duplicate likes from same email

class otpData(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.email} - {self.otp}'
    
    def is_expired(self):
        return (timezone.now() - self.created_at).seconds > 300