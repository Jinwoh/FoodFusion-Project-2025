# apps/clientes/urls.py

from django.urls import path
from . import views



urlpatterns = [
    path('historial_cliente/<int:cliente_id>/', views.historial_cliente, name='historial_cliente'),
]
