#configuracion de rutas especifico de la aplicacion fotografo
from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicio),
    path('nuevoFotografo',views.nuevoFotografo),
    path('guardarFotografo',views.guardarFotografo),
    path('eliminarFotografo/<id>',views.eliminarFotografo)
    ]