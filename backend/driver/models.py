from django.db import models
from django.contrib.auth.models import User
import uuid

class Driver(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class DriverUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class PersonalDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    driver = models.OneToOneField(DriverUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class VehicleDetails(models.Model):
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_manufacturer = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
    vehicle_color = models.CharField(max_length=20)
    vehicle_registration_date = models.DateField()
    driver = models.OneToOneField(DriverUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_number