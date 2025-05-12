from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(Empleado)

admin.site.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_apellido', 'cedula', 'correo', 'telefono', 'rol')
    search_fields = ('nombre_apellido', 'cedula', 'rol')

@admin.register(ClienteHistorial)
class ClienteHistorialAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_apellido',
        'cedula',
        'correo',
        'telefono',
        'fecha_registro',
        'estado',
        'fecha_eliminacion'
    )

    list_filter = ('fecha_eliminacion',)

    def estado(self, obj):
        return "Inactivo" if obj.fecha_eliminacion else "Activo"
    estado.short_description = "Estado"






