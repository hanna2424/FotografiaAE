from django.db import models

# Create your models here.
class Camaras(models.Model):
    id=models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    resolucion = models.CharField(max_length=100)
    lente = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5} {6}"
        return fila.format(self.id, self.marca,self.modelo,self.tipo,self.resolucion,self.lente,self.precio )