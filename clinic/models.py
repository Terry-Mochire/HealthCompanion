from django.db import models

from country.models import Country, County, SubCounty
from service.models import Service


# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    doctor_in_charge = models.CharField(max_length=120, null=True, blank=True)
    list_of_services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.name
