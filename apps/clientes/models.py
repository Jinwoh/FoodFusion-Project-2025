from django.db import models

class Cliente(models.Model):
    id_clientes = models.AutoField(primary_key=True)  # `SERIAL` en PostgreSQL se mapea a `AutoField` en Django
    nombre_apellido = models.CharField(max_length=250)  # VARCHAR(250) en PostgreSQL
    cedula = models.BigIntegerField()  # BIGINT en PostgreSQL
    telefono = models.BigIntegerField()  # BIGINT en PostgreSQL
    email = models.EmailField(max_length=150)  # VARCHAR(150) en PostgreSQL, con validación de formato de email

    class Meta:
        managed = False  # No gestionamos la tabla (Django no intentará crearla ni eliminarla)
        db_table = 'clientes'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre_apellido