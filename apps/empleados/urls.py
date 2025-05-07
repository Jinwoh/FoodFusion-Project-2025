# apps/clientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ajusta según tus vistas
]
