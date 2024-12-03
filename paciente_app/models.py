from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.PositiveSmallIntegerField(primary_key=True)  # Definir id_paciente
    nombre = models.CharField(max_length=100)  # Campo id_producto
    apellidos = models.CharField(max_length=100)  # Campo id_cliente
    fechanacimiento = models.CharField(max_length=100)  # Campo calificación
    telefono = models.CharField(max_length=100)  # Campo comentario
    direccion = models.CharField(max_length=100)  # Cambié a DateField para solo manejar fecha
    fecharegistro = models.CharField(max_length=100)  # Campo estado

    def __str__(self):
        return self.nombre
