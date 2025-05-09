from django.contrib import admin
from django.urls import include, path

from restaurante import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.clientes.urls')),
    path('empleados/', include('apps.empleados.urls')),
    path('menu/', include('apps.menu.urls')),
    path('reservas/', include('apps.reservas.urls')),
]

