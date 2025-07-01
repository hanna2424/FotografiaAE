from django.shortcuts import render,redirect
from .models import Camaras
# Create your views here.
def inicio(request):
    listadoCamaras=Camaras.objects.all()
    return render(request,"inicio.html",{'camara':listadoCamaras})

def nuevaCamara(request):
    return render(request,"nuevaCamara.html")

def guardarCamara(request):
    marca=request.POST["marca"]
    modelo=request.POST["modelo"]
    tipo=request.POST["tipo"]
    resolucion=request.POST["resolucion"]
    lente=request.POST["lente"]
    precio=request.POST["precio"]
    nuevaCamara=Camaras.objects.create(marca=marca,modelo=modelo,tipo=tipo,resolucion=resolucion,lente=lente,precio=precio)
    return redirect('/')

def eliminarCamara(request,id):
    camaraEliminar=Camaras.objects.get(id=id)
    camaraEliminar.delete()
    return redirect('/')