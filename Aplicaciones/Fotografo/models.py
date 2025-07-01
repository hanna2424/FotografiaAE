from django.db import models

# Create your models here.
class Fotografos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    anios_experiencia = models.IntegerField()
    contacto = models.CharField(max_length=100)

    def __str__(self):
        fila="{0}: {1} {2} {3} {4} "
        return fila.format(self.id, self.nombre,self.especialidad,self.anios_experiencia,self.contacto)