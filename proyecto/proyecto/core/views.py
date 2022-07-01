from django.shortcuts import render, redirect

from core.forms import VehiculosForm
from .models import Vehiculo

# Create your views here.
class Persona:
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
        
def home(request):
    return render(request,'core/home.html')

def test(request):
    lista=["Pollo con Papas Fritas", "Pastel de Choclo", "Porortos Granados"]
    hijo=Persona("Alan Brito","2")
    
    contexto={"nombre":"Anita La Huerfanita",
              "comidas": lista,
              "hijo":hijo}
    
    return render(request,'core/test.html',contexto)

def listaVehiculos(request):
    #voy a cargar un objeto con el contenido de la BD
    #metodo all que es equivalente a: SELECT * FROM Tabla
    vehiculos=Vehiculo.objects.all()
    #necesito traspasar el objeto obtenido al contexto
    contexto={
        'vehiculos':vehiculos
    }
    return render(request,'core/listaVehiculos.html',contexto)

def form_vehiculo(request):
    contexto={
        'form':VehiculosForm()
    }
    #verifico formulario POST y rescato datos
    if request.method=='POST':
        #con request puedo rescatar los datos del form
        formulario=VehiculosForm(request.POST)
        #validar el formulario
        if formulario.is_valid:
            formulario.save()
            #agregamos mensaje de exito
            contexto['mensaje']="Guardado con Exito"
            
    return render(request, 'core/form_vehiculo.html', contexto)

def form_mod_vehiculo(request,id):
    #filtramos la búsqueda por patente
    vehiculo=Vehiculo.objects.get(patente=id) 
    contexto={
        'form':VehiculosForm(instance=vehiculo)
    }
    #verifico formulario POST y rescato datos
    if request.method=='POST':
        formulario=VehiculosForm(data=request.POST, instance=vehiculo)
        #valido
        if formulario.is_valid:
            #guardo
            formulario.save()
            #agrego mensaje
            contexto['mensaje']="Modificado Correctamente"

    return render(request, 'core/form_mod_vehiculo.html', contexto)

def form_del_vehiculo(request,id):
    #busco la info del vehiculo que se desea eliminar
    vehiculo=Vehiculo.objects.get(patente=id)
    #elimino
    vehiculo.delete()

    return redirect(to='listaVehiculos')