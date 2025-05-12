from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_apellido', 'cedula', 'telefono', 'correo')
    search_fields = ('nombre_apellido', 'correo')
 

admin.site.register(Cliente, ClienteAdmin)

# Personalización del título del panel de admin
admin.site.site_header = "Administración del Restaurante"
admin.site.site_title = "Panel del Restaurante"
admin.site.index_title = "Bienvenido al Panel"
