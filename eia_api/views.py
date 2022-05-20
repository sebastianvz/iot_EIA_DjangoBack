from platform import machine
from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from eia_api.models import *
from eia_api.serializer import *

# Create your views here.
class Create_machine(APIView):
  def post(self,request):
    try:
      machine_name=request.data["machine_name"]
      marca=request.data["marca"]

      Machines.objects.create(machine_name=machine_name,marca=marca)
      return Response (status=status.HTTP_200_OK)
    except Exception as e:

      return Response (e,status=status.HTTP_501_NOT_IMPLEMENTED)



  def get(self,request):
    content={}
    list_machine=Machines.objects.all()

    raw_machines=[]
    for i in list_machine:
      dict_send={}
      dict_send["machine_name"]=i.machine_name
      dict_send["marca"]=i.marca
      dict_send["fecha de compra"]=i.buy_date
      raw_machines.append(dict_send)
    content["listado de maquinas"]=raw_machines



    return Response (content,status=status.HTTP_200_OK)



class Create_dots(APIView):
  def post(self,request):
    try:
      print("s",request.data["value"])
      id_device=request.data["id_device"]
      value=request.data["value"]
      unit=request.data["units"]
      
      Dots.objects.create(devices_id=id_device ,value=float(value) ,units=unit)
      return Response (status=status.HTTP_200_OK)
    except Exception as e:
      print("error",e)
      return Response (e,status=status.HTTP_501_NOT_IMPLEMENTED)


class Get_dots(APIView):
  def get(self,request,codigo):
    content={}
    list_dots=Dots.objects.filter(devices_id=codigo)  
  
    raw_dots=DotSerializer(list_dots,many=True)
    

    content["listado de puntos"]=raw_dots.data
    return Response (content,status=status.HTTP_200_OK)
