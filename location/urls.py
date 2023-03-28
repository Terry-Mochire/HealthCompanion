from django.urls import path
from .views import *

urlpatterns = [
    path('search/', search_clinics_in_location, name='search'),
]
