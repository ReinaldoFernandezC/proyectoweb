from django.db import models

# Create your models here.
#modelo para categoria
class categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria=models.CharField(max_length=30, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

class especie(models.Model):
    idEspecie=models.IntegerField(primary_key=True, verbose_name='Id de la especie')
    nombreEspecie=models.CharField(max_length=30, verbose_name='Nombre de la especie')

    def __str__(self):
        return self.nombreEspecie

#modelo para articulos
class articulo(models.Model):
    idArticulo=models.IntegerField(max_length=50, primary_key=True, verbose_name='numero de producto')
    Precio=models.IntegerField(max_length=50, verbose_name="Precio ")
    especie= models.ForeignKey(especie,on_delete=models.CASCADE)
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idArticulo

