from datetime import datetime

from django.db import models

from clinic.models import Clinic


SERVICE_CHOICES = (
    ('Doctor Consultation', 'Doctor Consultation'),
    ('Well Baby Clinics', 'Well Baby Clinics'),
    ('Dental', 'Dental'),
    ('Optical', 'Optical'),
    ('Pharmacy', 'Pharmacy'),
    ('Laboratory', 'Laboratory'),
    ('Imaging', 'Imaging'),
    ('Physiotherapy', 'Physiotherapy'),
    ('Family Planning', 'Family Planning'),
    ('Nutrition', 'Nutrition'),
    ('Mental Health', 'Mental Health'),
    ('Other', 'Other'),
)

TIME_CHOICES = (
    ('8:00AM', '8:00AM'),
    ('8:30AM', '8:30AM'),
    ('9:00AM', '9:00AM'),
    ('9:30AM', '9:30AM'),
    ('10:00AM', '10:00AM'),
    ('10:30AM', '10:30AM'),
    ('11:00AM', '11:00AM'),
    ('11:30AM', '11:30AM'),
    ('12:00PM', '12:00PM'),
    ('12:30PM', '12:30PM'),
    ('1:00PM', '1:00PM'),
    ('1:30PM', '1:30PM'),
    ('2:00PM', '2:00PM'),
    ('2:30PM', '2:30PM'),
    ('3:00PM', '3:00PM'),
    ('3:30PM', '3:30PM'),
    ('4:00PM', '4:00PM'),
    ('4:30PM', '4:30PM'),
    ('5:00PM', '5:00PM'),
    ('5:30PM', '5:30PM'),
    ('6:00PM', '6:00PM'),
    ('6:30PM', '6:30PM'),
    ('7:00PM', '7:00PM'),
    ('7:30PM', '7:30PM'),
    ('8:00PM', '8:00PM'),
)


class FirebaseUser(models.Model):
    uid = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.display_name


class Appointment(models.Model):
    user = models.ForeignKey(FirebaseUser, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    service = models.CharField(max_length=255, choices=SERVICE_CHOICES, default='Doctor Consultation')
    day = models.DateField(default=datetime.now)
    time = models.CharField(choices=TIME_CHOICES, default='11:00AM', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.clinic} - {self.service} - {self.day} - {self.time}'

