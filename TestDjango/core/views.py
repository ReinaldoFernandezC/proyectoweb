from django.shortcuts import render
from .models import Productos

# Create your views here.

def home(request):
    
    producto= Productos.objects.all()

    datos = {
        'Productos': producto
    }
    return render(request, 'core/home.html', datos)