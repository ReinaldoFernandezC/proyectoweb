from django.urls import path
from .views import form_del_vehiculo, form_mod_vehiculo, home,test, listaVehiculos, form_vehiculo, form_mod_vehiculo, form_del_vehiculo

urlpatterns =[
    #path('' , home, name="home"),
    path('' , test, name="test"),
    path('lista-Vehiculos' , listaVehiculos, name="listaVehiculos"),
    path('form-Vehiculos' , form_vehiculo, name="form_vehiculo"),
    path('form-mod-Vehiculos/<id>' , form_mod_vehiculo, name="form_mod_vehiculo"),
    path('form-del-Vehiculos/<id>' , form_del_vehiculo, name="form_del_vehiculo"),
]