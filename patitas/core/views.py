from django.shortcuts import render, redirect

from core.forms import ArticulosForm
from .models import Articulo

def test(request):

    return render(request,'core/test.html')   

def listaArticulos(request):
    articulos=Articulo.objects.all()
    contexto={
        'articulos':articulos
    }
    return render(request, 'core/test.html', contexto)


def form_articulo(request):
    contexto={
        'form':ArticulosForm()
    }
    if request.method=='POST':
        formulario=ArticulosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje']="Guardado con Exito"
            
    return render(request, 'core/form_articulo.html', contexto)

def form_mod_articulo(request,id):
    articulo=Articulo.objects.get(idArticulo=id) 
    contexto={
        'form':ArticulosForm(instance=articulo)
    }
    if request.method=='POST':
        formulario=ArticulosForm(data=request.POST, instance=articulo)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje']="Modificado Correctamente"

    return render(request, 'core/form_mod_articulo.html', contexto)

def form_del_articulo(request,id):
    articulo=Articulo.objects.get(idArticulo=id)
    articulo.delete()

    return redirect(to='listaArticulos')