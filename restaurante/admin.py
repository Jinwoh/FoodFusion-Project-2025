from django.contrib import admin
from ..apps.clientes.models import Cliente
from ..apps.reservas.models import CategoriaMenu, Menu, Mesa, Reserva, Empleado, Pedido, DetallePedido
from django.contrib import admin


from ..apps.reservas.models import ClienteHistorial

@admin.register(ClienteHistorial)
class ClienteHistorialAdmin(admin.ModelAdmin):
    list_display = ('nombre_apellido', 'correo', 'cedula', 'telefono', 'fecha_registro', 'fecha_eliminacion')
    search_fields = ('correo', 'cedula', 'nombre_apellido')
    list_filter = ('fecha_eliminacion',)

    
admin.site.site_header = "Panel de Administración"
admin.site.index_title = "Panel"
admin.site.site_title = "FoodFusion"


admin.site.register(CategoriaMenu)
admin.site.register(Menu)
admin.site.register(Cliente)
admin.site.register(Mesa)
admin.site.register(Reserva)
admin.site.register(Empleado)
admin.site.register(Pedido)
admin.site.register(DetallePedido)