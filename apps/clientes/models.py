from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=250)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=150)

    class Meta:
        db_table = 'clientes'
        managed = False
