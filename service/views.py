import generic as generic
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from clinic.models import Clinic
from service.models import Service
from django.views import generic


# Create your views here.


def get_services(request):
    allServices = Service.objects.all()
    data = serialize('json', allServices)
    return HttpResponse(data, content_type="application/json")


def get_service_by_id(request, pk):
    service = Service.objects.get(pk=pk)
    data = serialize('json', [service])
    return HttpResponse(data, content_type="application/json")


def get_services_in_clinic(request, pk):
    service = Service.objects.filter(clinic__id=pk)
    data = serialize('json', service)
    return HttpResponse(data, content_type="application/json")


def search_clinics_with_service(request, service_name):
    clinics = Clinic.objects.filter(list_of_services__name=service_name)
    return render(request, "clinic/clinic_list.html", {"clinics": clinics})
