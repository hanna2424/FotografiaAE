from django.db import models

# Create your models here.
class Sesiones(models.Model):
    id=models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    tipo_sesion = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fotografo = models.CharField(max_length=100)  

    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5} {6} {7} "
        return fila.format(self.id, self.nombre_cliente,self.fecha,self.lugar,self.duracion,self.tipo_sesion,self.costo,self.fotografo )