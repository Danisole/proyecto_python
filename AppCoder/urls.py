from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp, name="inicioApp"),
    path('crear_paquete/', crear_paquete),
    path("suscriptor/", suscriptor, name="suscriptor"),
    path("itinerario/", itinerario, name="itinerario"),
    path("eliminarSuscriptor/<id>", eliminarSuscriptor, name="eliminarSuscriptor"),
]