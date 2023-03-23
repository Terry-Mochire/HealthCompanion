from django.shortcuts import render
from django.views import generic

from .models import Clinic


# Create your views here.

class ClinicListView(generic.ListView):
    model = Clinic
    template_name = 'clinic/clinic_list.html'
    context_object_name = 'clinics'

    def get_queryset(self):
        return Clinic.objects.all()


class ClinicDetailView(generic.DetailView):
    model = Clinic
    template_name = 'clinic/clinic_detail.html'
    context_object_name = 'clinic'


def about_us(request):
    return render(request, 'about_us.html')


def our_services(request):
    return render(request, 'our_services.html')

def search_by_name(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    clinics = Clinic.objects.filter(name__contains=search_text)
    return render(request, 'clinic/clinic_list.html', {'clinics': clinics})
