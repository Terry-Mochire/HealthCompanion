from django.contrib import admin

# Register your models here.
from django.contrib import admin

from location.models import Country, County, SubCounty

# Register your models here.
admin.site.register(Country)
admin.site.register(County)
admin.site.register(SubCounty)