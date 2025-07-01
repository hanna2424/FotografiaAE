from django.shortcuts import render,redirect
from .models import Fotografos
# Create your views here.
def inicio(request):
    listadoFotografos=Fotografos.objects.all()
    return render(request,"iniciof.html",{'fotografo':listadoFotografos})

def nuevoFotografo(request):
    return render(request,"nuevoFotografo.html")

def guardarFotografo(request):
    nombre=request.POST["nombre"]
    especialidad=request.POST["especialidad"]
    anios_experiencia=request.POST["anios_experiencia"]
    contacto=request.POST["contacto"]
    nuevoFotografo=Fotografos.objects.create(nombre=nombre,especialidad=especialidad,anios_experiencia=anios_experiencia,contacto=contacto)
    return redirect('/')

def eliminarFotografo(request,id):
    fotografoEliminar=Fotografos.objects.get(id=id)
    fotografoEliminar.delete()
    return redirect('/')