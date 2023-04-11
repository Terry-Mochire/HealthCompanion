from django.urls import path
from .views import *

urlpatterns = [
    path("save_user", save_user, name="save_user"),
    path("get_user/<str:user_id>", get_user, name="get_user"),
    path("booking", booking, name="booking"),
    path("booking_submit/<str:user_id>", booking_submit, name="booking_submit"),
    path("get_bookings/<str:user_id>", get_appointments, name="get_bookings"),
    path("clinic/appointments/<int:booking_id>", get_appointments_by_clinic, name="get_appointments_by_clinic"),
]
