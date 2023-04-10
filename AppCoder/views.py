from django.shortcuts import render
from .models import *
from .forms import SuscriptorForm
from django.http import HttpResponse

# Create your views here.

def  crear_paquete(request):

    nombre_paquete="paquete aventurero"
    cantidad_personas=3

    viaje=Viaje(nombre=nombre_paquete,  personas=cantidad_personas)
    viaje.save()

    respuesta=f"Su paquete  --{nombre_paquete} para {cantidad_personas} personas fue creado satisfactoriamente"

    return HttpResponse(respuesta)

def suscriptor(request):

    if request.method =="POST":

        form = SuscriptorForm(request.POST)

        if form.is_valid():
        
            suscriptor = Suscriptor()

            suscriptor.nombre = form.cleaned_data['nombre']
            suscriptor.apellido = form.cleaned_data['apellido']
            suscriptor.email = form.cleaned_data['email']
            suscriptor.save()

            form = SuscriptorForm()

    else:
        form = SuscriptorForm()
    
    suscriptor= Suscriptor.objects.all()
    context = {"suscriptor": suscriptor}

    return render(request, "AppCoder/suscriptor.html", context)


def itinerario(request):
    return render(request, "AppCoder/itinerario.html")

def inicio(request):
    return HttpResponse("mi pagina de inicio")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")