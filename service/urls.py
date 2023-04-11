from django.urls import path
from .views import *

urlpatterns = [
    path("services", get_services, name="services"),
    path("service/<int:pk>", get_service_by_id, name="service_by_id"),
    path("services_in_clinic/<int:pk>", get_services_in_clinic, name="services_in_clinic"),
    path("search_clinics_with_service/<str:service_name>", search_clinics_with_service,
         name="search_clinics_with_service"),
]
