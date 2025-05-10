from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(Empleado)


admin.site.register(ClienteHistorial)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_apellido', 'cedula', 'correo', 'telefono', 'rol')
    search_fields = ('nombre_apellido', 'cedula', 'rol')

