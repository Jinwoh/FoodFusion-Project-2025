from django.urls import path
from . import views

urlpatterns = [
    path('', views.mis_datos, name='mis_datos'), 
    path('signup/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.signout, name='logout'),
    path('mis_datos/', views.mis_datos, name='mis_datos'),
    path('eliminar-cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('editar_datos/', views.editar_datos, name='editar_datos'), # Ajusta según tus vistas
]