"""patitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import form_del_articulo, form_del_articulo, form_mod_articulos, listaArticulos, form_articulo, form_mod_articulos, form_del_articulo,test

urlpatterns =[

    #path('' , home, name="home"),   
    path('' , test, name="test"),
    path('listaArticulos' , listaArticulos, name="listaArticulos"),
    path('form-Vehiculos' , form_articulo, name="form_articulo"),
    path('form-mod-Vehiculos/<id>' , form_mod_articulos, name="form_mod_vehiculo"),
    path('form-del-Vehiculos/<id>' , form_del_articulo, name="form_del_vehiculo"),
]
