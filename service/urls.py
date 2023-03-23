from django.urls import path
from .views import *

urlpatterns = [
    path("services", ServiceListView.as_view(), name="services"),
    path("service_detail/<int:pk>", ServiceDetailView.as_view(), name="service_detail"),
    path("search_clinics_with_service/<str:service_name>", search_clinics_with_service, name="search_clinics_with_service"),
]