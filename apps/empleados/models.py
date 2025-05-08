from django.db import models

# Create your models here.
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20)
    correo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    rol = models.CharField(max_length=20)

    class Meta:
        db_table = 'empleados'
        managed = False