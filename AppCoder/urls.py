from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp),
    path('crear_paquete/', crear_paquete),
    path("suscriptor/", suscriptor),
    path("itinerarios/", itinerarios),
]