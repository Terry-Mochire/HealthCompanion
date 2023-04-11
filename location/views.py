import json

from django.core.serializers import serialize
from django.http import HttpResponse

from clinic.models import Clinic
from location.models import Country, County, SubCounty

# Create your views here.


countries = Country.objects.all()
counties = County.objects.all()
sub_counties = SubCounty.objects.all()


def get_countries(request):
    allCountries = Country.objects.all()
    data = serialize('json', allCountries)
    return HttpResponse(data, content_type="application/json")


def get_counties(request):
    allCounties = County.objects.all()
    data = serialize('json', allCounties)
    return HttpResponse(data, content_type="application/json")


def get_sub_counties(request):
    allSubCounties = SubCounty.objects.all()
    data = serialize('json', allSubCounties)
    return HttpResponse(data, content_type="application/json")


def get_sub_counties_by_county(request, county_id):
    allSubCounties = SubCounty.objects.filter(county__id=county_id)
    data = serialize('json', allSubCounties)
    return HttpResponse(data, content_type="application/json")


def search_clinics_in_location(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')

        data_dict = json.loads(data)
        country_id = data_dict.get('country')
        county_id = data_dict.get('county')
        sub_county_id = data_dict.get('sub_county')
        print(country_id, county_id, sub_county_id)
        if country_id:
            clinics = Clinic.objects.filter(country__id=country_id)
        if county_id:
            clinics = Clinic.objects.filter(country__id=country_id, county__id=county_id)
        if sub_county_id:
            clinics = Clinic.objects.filter(country__id=country_id, county__id=county_id, sub_county__id=sub_county_id)
        else:
            clinics = Clinic.objects.all()
        data = serialize('json', clinics)
        return HttpResponse(data, content_type="application/json")
