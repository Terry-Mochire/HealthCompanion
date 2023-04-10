from django.urls import path
from .views import *

urlpatterns = [
    path("get_csrf_token", get_csrf_token, name="get_csrf_token"),
    path("clinics", clinics, name="clinics"),
    path("clinic_detail/<int:pk>", clinic_detail, name="clinic_detail"),
    path("search_by_name/<str:name>", search_by_name, name="search_by_name"),
]
