from pyexpat import model
from django.db import models

# Create your models here.

class CategoriaP(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
    def __str__(self):
        return self.nombreCategoria

#Modelo para Productos
class Productos(models.Model):
    idProducto =models.IntegerField(primary_key=True, verbose_name='Id del Producto')
    nombreProducto =models.CharField(max_length=64, verbose_name='Nombre del Producto')
    descripcion =models.CharField(max_length=64, verbose_name='Descripcion del Producto')
    precio = models.IntegerField()
    categoria = models.ForeignKey(CategoriaP, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreProducto
