from django.contrib import admin
from .models import Mesa, Reserva
# Register your models here.

admin.site.register(Mesa)
#admin.site.register(Reserva)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'clientes', 'mesa')
    list_filter = ('fecha_reserva',)
    search_fields = ('clientes__nombre_apellido',)