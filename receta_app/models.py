from django.db import models

class Receta(models.Model):
    id_pedido=models.PositiveSmallIntegerField(primary_key=True)
    id_cliente=models.IntegerField()
    fecha_receta=models.CharField(max_length=100)
    total_pedido=models.IntegerField()
    estado_pedido=models.CharField(max_length=100)
    metodo_pago=models.CharField(max_length=100)
    direccion_envio=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id_pedido)
