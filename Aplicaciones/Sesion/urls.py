#configuracion de rutas especifico de la aplicacion empresas
from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicio, name='inicio_sesion'),
    path('nuevaSesion',views.nuevaSesion,name='nueva_sesion'),
    path('guardarSesion',views.guardarSesion,name='guardar_sesion'),
    path('eliminarSesion/<id>',views.eliminarSesion,name='eliminar_sesion')
    ]