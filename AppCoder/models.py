from django.db import models

# Create your models here.
class Viaje(models.Model):

    nombre=models.CharField(max_length=50)
    personas=models.IntegerField()

class Suscriptor(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Itinerario(models.Model):

    nombre=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    empresa=models.CharField(max_length=50)