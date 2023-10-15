from django.shortcuts import render
from Servicios.models import Servicio
# Create your views here.

# Vista de servicios
def services(request):
    servicios = Servicio.objects.all()
    return render(request, "Servicios/servicios.html", {"servicios": servicios})