from django.contrib import admin
from .models import Event, EventRequest, otpData, EventLike

# Register your models here.
admin.site.register(Event)
admin.site.register(otpData)
admin.site.register(EventLike)
admin.site.register(EventRequest)