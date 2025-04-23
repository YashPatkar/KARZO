from django.contrib import admin
from .models import DriverFeedback, DriverUser, PersonalDetails, VehicleDetails, DriverRegistrationToken
# Register your models here.
admin.site.register(DriverUser)
admin.site.register(PersonalDetails)
admin.site.register(VehicleDetails)
admin.site.register(DriverRegistrationToken)
admin.site.register(DriverFeedback)