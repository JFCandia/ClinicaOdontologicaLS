from django.shortcuts import render
from django.db import connection

       
def login(request):
    return render(request,'core/login.html',{})

def inicio(request):
    return render(request,'core/inicio.html',{}) 

def horacancelada(request):
    return render(request,'core/horacancelada.html',{})

def horaexitosa(request):
    return render(request,'core/horaexitosa.html',{})

def proxatenciones(request):
    return render(request,'core/proxatenciones.html',{})

def registro(request):
    return render(request,'core/registro.html',{}) 

def resumensolicitud(request):
    return render(request,'core/resumensolicitud.html',{}) 

def tomarhora(request):
    return render(request,'core/tomarhora.html',{}) 

def vermishoras(request):
    return render(request,'core/vermishoras.html',{})    

                 

