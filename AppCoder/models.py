from django.db import models

# Create your models here.
class Viaje(models.Model):

    nombre=models.CharField(max_length=50)
    personas=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.personas}"

class Suscriptor(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"

class Itinerario(models.Model):

    nombre=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    empresa=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.lugar} {self.empresa}"