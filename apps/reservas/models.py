from django.db import models
from apps.clientes.models import Cliente


# Create your models here.
class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    nro_mesa = models.IntegerField()
    capacidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mesa'

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('clientes.Cliente', on_delete=models.DO_NOTHING, db_column='id_cliente')
    id_mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING, db_column='id_mesa')
    estado = models.CharField(max_length=25)
    fecha_reserva = models.DateField()

    class Meta:
        managed = False
        db_table = 'reserva'

Mesa.add_to_class('reserva_id', models.ForeignKey('Reserva', on_delete=models.DO_NOTHING, db_column='reserva_id', null=True, blank=True))
