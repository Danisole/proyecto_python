from django import forms

class SuscriptorForm(forms.Form):

    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()