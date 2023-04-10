from django.shortcuts import render
from .models import *
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
    return render(request, "AppCoder/suscriptor.html")

def itinerario(request):
    return render(request, "AppCoder/itinerario.html")

def inicio(request):
    return HttpResponse("mi pagina de inicio")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")