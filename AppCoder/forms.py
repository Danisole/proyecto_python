from django import forms

class SuscriptorForm(forms.Form):

    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()

class ComentariosForm(forms.Form):

    nombre=forms.CharField(max_length=50)
    reseña=forms.CharField(max_length=140)
    estrellas=forms.IntegerField()  


class ItinerarioForm(forms.Form):

    nombre=forms.CharField(max_length=50)
    lugar=forms.CharField(max_length=50)
    empresa=forms.CharField(max_length=50)