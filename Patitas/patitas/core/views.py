from django.shortcuts import render, redirect

from core.forms import articuloForm
from .models import articulo

def test(request):
    return render(request,'core/test.html')   

def listaArticulos(request):
    #voy a cargar un objeto con el contenido de la BD
    #metodo all que es equivalente a: SELECT * FROM Tabla
    articulo=articulo.objects.all()
    #necesito traspasar el objeto obtenido al contexto
    contexto={
        'articulo':articulo
    }
    return render(request,'core/listaArticulo.html',contexto)

def form_articulo(request):
    contexto={
        'form':articuloForm()
    }
    #verifico formulario POST y rescato datos
    if request.method=='POST':
        #con request puedo rescatar los datos del form
        formulario=articuloForm(request.POST)
        #validar el formulario
        if formulario.is_valid:
            formulario.save()
            #agregamos mensaje de exito
            contexto['mensaje']="Guardado con Exito"
            
    return render(request, 'articuloForm.html', contexto)

def form_mod_articulos(request,id):
    #filtramos la búsqueda por patente
    articulo=articulo.objects.get(idArticulo=id) 
    contexto={
        'form':articuloForm(instance=articulo)
    }
    #verifico formulario POST y rescato datos
    if request.method=='POST':
        formulario=articuloForm(data=request.POST, instance=articulo)
        #valido
        if formulario.is_valid:
            #guardo
            formulario.save()
            #agrego mensaje
            contexto['mensaje']="Modificado Correctamente"

    return render(request, 'core/form_mod_vehiculo.html', contexto)

def form_del_articulo(request,id):
    #busco la info del vehiculo que se desea eliminar
    articulo=articulo.objects.get(idArticulo=id)
    #elimino
    articulo.delete()

    return redirect(to='listaArticulos')