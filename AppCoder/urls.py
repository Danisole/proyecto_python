from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp, name="inicioApp"),
    path('crear_paquete/', crear_paquete),

    path("comentarios/", comentarios, name="comentarios"),
    
    path("itinerario/", itinerario, name="itinerario"),

    path("suscriptor/", suscriptor, name="suscriptor"),
    path("eliminarSuscriptor/<id>", eliminarSuscriptor, name="eliminarSuscriptor"),
]