from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
@login_required

def index(request):
    return render(request, 'core/home.html')

def salir(request):
    logout(request)
    return redirect('/')