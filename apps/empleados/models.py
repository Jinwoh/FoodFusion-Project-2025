from django.db import models

class Empleado(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    celular = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_apellido