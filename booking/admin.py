from django.contrib import admin

from booking.models import Appointment, FirebaseUser

# Register your models here.
admin.site.register(Appointment)
admin.site.register(FirebaseUser)
