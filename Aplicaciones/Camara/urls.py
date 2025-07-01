#configuracion de rutas especifico de la aplicacion empresas
from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicio, name='inicio_camara'),
    path('nuevaCamara',views.nuevaCamara, name='nueva_camara'),
    path('guardarCamara',views.guardarCamara, name='guardar_camara'),
    path('eliminarCamara/<id>',views.eliminarCamara, name='eliminar_camara')
    ]