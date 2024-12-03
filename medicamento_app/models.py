from django.db import models

# Create your models here.

class Medicamento(models.Model):
    id_producto=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    volumen=models.CharField(max_length=100)
    precio=models.CharField(max_length=100)
    notas_olfativas=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre