from django.shortcuts import render

from clinic.models import Clinic
from location.forms import LocationForm
from location.models import Country, County, SubCounty

# Create your views here.


countries = Country.objects.all()
counties = County.objects.all()
sub_counties = SubCounty.objects.all()


def search_clinics_in_location(request):
    if request.method == 'POST':
        country_id = request.POST.get('country')
        county_id = request.POST.get('county')
        sub_county_id = request.POST.get('sub_county')

        print(country_id, county_id, sub_county_id)

        clinics = Clinic.objects.filter(country=country_id, county=county_id, sub_county=sub_county_id)
        return render(request, 'clinic/clinic_list.html', {'clinics': clinics})
    else:
        form = LocationForm()
    return render(request, 'location/search.html', {'form': form, 'countries': countries, 'counties': counties,
                                                    'sub_counties': sub_counties})
