# Generated by Django 4.1.7 on 2023-03-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0002_alter_clinic_country_delete_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="clinic",
            name="doctor_in_charge",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="clinic",
            name="email",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="clinic",
            name="telephone",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
