from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ajusta según tus vistas
    path('', views.mis_datos, name='mis_datos'),  # Ajusta según tus vistas
]