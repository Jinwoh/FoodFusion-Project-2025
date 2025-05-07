from django.db import models
from apps.empleados.models import Empleado
from apps.reservas.models import Mesa, Reserva
from apps.clientes.models import Cliente



# Create your models here.
class MenuCategoria(models.Model):
    id_menu_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'menu_categoria'
    def __str__(self):
        return self.nombre    

class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField()
    img_url = models.TextField(null=True)
    id_categoria = models.ForeignKey(MenuCategoria, on_delete=models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'menu'

class Pedidos(models.Model):
    id_pedidos = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.DO_NOTHING, db_column='cliente_id')
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING, db_column='mesa_id')
    empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='empleado_id')
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, db_column='menu_id')
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20)
    comentario = models.CharField(max_length=250, null=True)
    fecha_actualizacion = models.DateField()
    reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING, db_column='reserva_id')

    class Meta:
        managed = False
        db_table = 'pedidos'