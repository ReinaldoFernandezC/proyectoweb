from django.contrib import admin
from .models import categoria,especie, articulo
# Register your models here.

admin.site.register(categoria)
admin.site.register(especie)
admin.site.register(articulo)