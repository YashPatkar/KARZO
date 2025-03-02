from django.contrib import admin
from .models import DriverUser, PersonalDetails, VehicleDetails
# Register your models here.
admin.site.register(DriverUser)
admin.site.register(PersonalDetails)
admin.site.register(VehicleDetails)