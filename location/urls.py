from django.urls import path
from .views import *

urlpatterns = [
    path('search/', search_clinics_in_location, name='search'),
    path('countries', get_countries, name='get_countries'),
    path('counties', get_counties, name='get_counties'),
    path('sub_counties', get_sub_counties, name='get_sub_counties'),
    path('sub_county/<int:county_id>', get_sub_counties_by_county, name='get_sub_counties_by_county'),
]
