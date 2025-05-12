from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Cliente
from apps.empleados.models import ClienteHistorial

@receiver(post_save, sender=Cliente)
def crear_historial_al_registrar_cliente(sender, instance, created, **kwargs):
    if created:
        ClienteHistorial.objects.create(
            nombre_apellido=instance.nombre_apellido,
            cedula=instance.cedula,
            correo=instance.correo,
            telefono=instance.telefono,
            fecha_registro=now()
        )

@receiver(post_delete, sender=Cliente)
def guardar_historial_al_eliminar_cliente(sender, instance, **kwargs):
    try:
        historial = ClienteHistorial.objects.get(correo=instance.correo)
        historial.fecha_eliminacion = now()
        historial.save()
    except ClienteHistorial.DoesNotExist:
        ClienteHistorial.objects.create(
            nombre_apellido=instance.nombre_apellido,
            cedula=instance.cedula,
            correo=instance.correo,
            telefono=instance.telefono,
            fecha_registro=now(),
            fecha_eliminacion=now()
        )
