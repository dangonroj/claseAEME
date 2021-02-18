from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

# Ejemplo 1 holaMundo - HttpResponse
def holaMundo(request):
    return HttpResponse("Hola mundo")

# Ejemplo 2 holaMundo2 - render(request, "plantilla.html")
def holaMundo2(request):
    return render(request,"holaMundo2.html")

# Ejemplo 3 calendario - con paso de variable date.today()
def calendario(request):
    fecha = date.today()
    return render(request,"calendario.html",{'fecha':fecha})

# Ejemplo 4 calculadora - urls con parámetros
def calculadora(request,a,b):
   numA = int(a)
   numB = int(b)
   suma = numA + numB
   resta = numA - numB
   return render(request, 'calculadora.html',{'numA':numA, 'numB':numB, 'suma': suma, 'resta':resta})


