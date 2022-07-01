from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Articulo

class ArticulosForm(ModelForm):
    class Meta:
        model=Articulo
        fields=['idArticulo','precio','nombreProducto','especie','categoria']