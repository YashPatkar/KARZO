from django.contrib import admin
from .models import RegistrationToken, PassengerUser, PersonalDetails
# Register your models here.
admin.site.register(RegistrationToken)
admin.site.register(PassengerUser)
admin.site.register(PersonalDetails)