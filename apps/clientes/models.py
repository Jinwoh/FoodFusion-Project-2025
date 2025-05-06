from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    # Esto es un comentario cualquiera.
    def __str__(self):
        return f"{self.nombre_apellido} ({self.cedula})"
    

class ClienteHistorial(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    fecha_registro = models.DateTimeField()
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_apellido} ({self.correo})"