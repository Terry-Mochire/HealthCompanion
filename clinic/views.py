from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views import generic

from .models import Clinic


# Create your views here.

def clinics(request):
    allClinics = Clinic.objects.all()
    data = serialize('json', allClinics)
    return HttpResponse(data, content_type="application/json")


def clinic_detail(request, pk):
    clinic = Clinic.objects.get(pk=pk)
    data = serialize('json', [clinic], fields=('name', 'country', 'county', 'sub_county', 'telephone', 'email', 'doctor_in_charge', 'list_of_services'))
    return HttpResponse(data, content_type="application/json")


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})


def search_by_name(request, name):
    if request.method == 'POST':
        search_text = name
    else:
        search_text = ''
    clinic_by_name = Clinic.objects.filter(name__contains=search_text)
    return HttpResponse(serialize('json', clinic_by_name), content_type="application/json")
