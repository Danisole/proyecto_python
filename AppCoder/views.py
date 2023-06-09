from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

from django.urls import reverse_lazy
# Create your views here.

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

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
    context = {"suscriptor": suscriptor, "form" : form}

    return render(request, "AppCoder/suscriptor.html", context)

def eliminarSuscriptor(request, id):
    suscriptor = Suscriptor.objects.get(id=id)
    print(suscriptor)
    suscriptor.delete()
    suscriptor= Suscriptor.objects.all()
    form = SuscriptorForm()
    return render(request, "AppCoder/suscriptor.html", {"suscriptor": suscriptor, "mensaje": "Tu suscripcion fue eliminada con exito", "form" : form})


def busquedaItinerario(request):
    return render(request, "AppCoder/busquedaItinerario.html")


def buscar(request):
    region=request.GET["region"]
    print(region)

    if region!="":

        itinerarios=Itinerarios.objects.filter(region__icontains=region)
        return render(request, "AppCoder/buscar.html", {"itinerarios": itinerarios})
    
    else:
        return render(request, "AppCoder/buscar.html", {"mensaje":"campo vacio"})


def comentarios(request):

    if request.method =="POST":

        form = ComentariosForm(request.POST)

        if form.is_valid():
        
            comentarios = Comentarios()

            comentarios.nombre = form.cleaned_data['nombre']
            comentarios.reseña = form.cleaned_data['reseña']
            comentarios.estrellas = form.cleaned_data['estrellas']
            comentarios.save()

            form = ComentariosForm()

    else:
        form = ComentariosForm()
    
    comentarios= Comentarios.objects.all()
    context = {"comentarios": comentarios, "form" : form}

    return render(request, "AppCoder/comentarios.html", context)



def inicio(request):
    return HttpResponse("mi pagina de inicio")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")

#login logout register

def login_request(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {"mensaje": f"usuario {usu} logueado correctamentre"})
            else:
                return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})    
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {"form": form})
        
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=UserCreationForm()
        return render(request, "AppCoder/register.html", {"form": form})    