from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=150)
    cedula = models.BigIntegerField()
    correo = models.CharField(max_length=150)
    telefono = models.BigIntegerField(null=True)
    rol = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'empleado'