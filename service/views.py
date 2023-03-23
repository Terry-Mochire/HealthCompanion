import generic as generic
from django.shortcuts import render

from clinic.models import Clinic
from service.models import Service
from django.views import generic


# Create your views here.

class ServiceListView(generic.ListView):
    model = Service
    template_name = "service/services.html"
    context_object_name = "services"

    def get_queryset(self):
        return Service.objects.all()


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = "service/service_detail.html"
    context_object_name = "service"


def search_clinics_with_service(request, service_name):
    clinics = Clinic.objects.filter(list_of_services__name=service_name)
    return render(request, "clinic/clinic_list.html", {"clinics": clinics})
