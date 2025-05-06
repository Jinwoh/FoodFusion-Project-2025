from django.db import models # type: ignore


class Reserva(models.Model):
    fecha_reserva = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.cliente.nombre_apellido} para {self.fecha_reserva}"







    





