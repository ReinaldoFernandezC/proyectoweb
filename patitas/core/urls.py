
from django.urls import path
from .views import form_del_articulo, listaArticulos, form_articulo, form_mod_articulo, form_del_articulo,test

urlpatterns =[

    #path('' , home, name="home"),   
    path('' , test, name="test"),
    path('listaArticulos' , listaArticulos, name="listaArticulos"),
    path('form-Vehiculos' , form_articulo, name="form_articulo"),
    path('form_mod_articulo' , form_mod_articulo, name="form_mod_articulo"),
    path('form_mod_articulo' , form_del_articulo, name="form_mod_articulo"),
]
