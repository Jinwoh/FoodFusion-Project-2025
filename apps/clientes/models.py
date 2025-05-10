from django.db import models


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=250)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=150, unique=True)
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'
        managed = False

class ClienteHistorial(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    fecha_registro = models.DateTimeField()
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_apellido} ({self.correo})"