from django.db import models
from apps.clientes.models import Cliente


class Mesa(models.Model):
    id = models.AutoField(primary_key=True)
    nro_mesa = models.IntegerField()
    capacidad_personas = models.IntegerField()

    class Meta:
        db_table = 'mesa'
        managed = False


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    clientes = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='clientes_id')
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING, db_column='mesa_id')

    class Meta:
        db_table = 'reserva'
        managed = False
