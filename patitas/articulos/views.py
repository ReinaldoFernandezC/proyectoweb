from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Articulo
from .serializers import ArticuloSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_vehiculos(request):
    #verificar si es llamada POST o GET
    if request.method=='GET':
        #buscar todos los vehículos (SELECT *....)
        articulo=Articulo.objects.all()
        serializer=ArticuloSerializer(articulo, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ArticuloSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT', 'DELETE'])
def detalle_articulo(request,id):
    #valido que la patente exista
    try:
        articulo=Articulo.objects.get(patente=id)
    except Articulo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #verificar el método invocado
    if request.method=='GET': #devolver info de UN vehiculo por su patente
        serializer=ArticuloSerializer(articulo)
        return Response(serializer.data)
    elif request.method=='PUT':#actualizar UN vehiculo por su patente
        data=JSONParser().parse(request)
        serializer=ArticuloSerializer(articulo,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':#Eliminar UN vehiculo por su patente
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)