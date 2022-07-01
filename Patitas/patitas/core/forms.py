from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import articulo

class articuloForm(ModelForm):
    class Meta:
        model=articulo
        fields=['idArticulo','Precio','especie','categoria']