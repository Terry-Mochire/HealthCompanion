from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
