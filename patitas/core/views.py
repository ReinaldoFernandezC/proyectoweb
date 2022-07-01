from django.shortcuts import render, redirect

from core.forms import ArticulosForm
from .models import Articulo

def test(request):

    return render(request,'core/test.html')   

def listaArticulos(request):
    #voy a cargar un objeto con el contenido de la BD
    #metodo all que es equivalente a: SELECT * FROM Tabla
    articulos=Articulo.objects.all()
    #necesito traspasar el objeto obtenido al contexto
    contexto={
        'articulos':articulos
    }


def form_articulo(request):
    contexto={
        'form':ArticulosForm()
    }
    #verifico formulario POST y rescato datos
    if request.method=='POST':
        #con request puedo rescatar los datos del form
        formulario=ArticulosForm(request.POST)
        #validar el formulario
        if formulario.is_valid:
            formulario.save()
            #agregamos mensaje de exito
            contexto['mensaje']="Guardado con Exito"
            
    return render(request, 'core/form_articulo.html', contexto)

def form_mod_articulo(request,id):
    #filtramos la búsqueda por patente
    articulo=Articulo.objects.get(idArticulo=id) 
    contexto={
        'form':ArticulosForm(instance=articulo)
    }
    #verifico formulario POST y rescato datos
    if request.method=='POST':
        formulario=ArticulosForm(data=request.POST, instance=articulo)
        #valido
        if formulario.is_valid:
            #guardo
            formulario.save()
            #agrego mensaje
            contexto['mensaje']="Modificado Correctamente"

    return render(request, 'core/form_mod_articulo.html', contexto)

def form_del_articulo(request,id):
    #busco la info del vehiculo que se desea eliminar
    articulo=Articulo.objects.get(idArticulo=id)
    #elimino
    articulo.delete()

    return redirect(to='listaArticulos')