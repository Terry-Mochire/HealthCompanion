from django.urls import path
from .views import *

urlpatterns = [
    path("", about_us, name="about_us"),
    path("clinics", ClinicListView.as_view(), name="clinics"),
    path("clinic_detail/<int:pk>", ClinicDetailView.as_view(), name="clinic_detail"),
    path("search_by_name", search_by_name, name="search_by_name"),
]