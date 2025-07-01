from django.shortcuts import render,redirect
from .models import Sesiones
# Create your views here.
def inicio(request):
    listadoSesiones=Sesiones.objects.all()
    return render(request,"inicioS.html",{'sesion':listadoSesiones})

def nuevaSesion(request):
    return render(request,"nuevaSesion.html")

def guardarSesion(request):
    nombre_cliente=request.POST["nombre_cliente"]
    fecha=request.POST["fecha"]
    lugar=request.POST["lugar"]
    duracion=request.POST["duracion"]
    tipo_sesion=request.POST["tipo_sesion"]
    costo=request.POST["costo"]
    fotografo=request.POST["fotografo"]
    nuevoSesiones=Sesiones.objects.create(nombre_cliente=nombre_cliente,fecha=fecha,lugar=lugar,duracion=duracion,tipo_sesion=tipo_sesion,costo=costo,fotografo=fotografo)
    return redirect('/')

def eliminarSesion(request,id):
    sesionEliminar=Sesiones.objects.get(id=id)
    sesionEliminar.delete()
    return redirect('/')