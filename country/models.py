from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=120)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCounty(models.Model):
    name = models.CharField(max_length=120)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
