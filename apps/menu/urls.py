from django.urls import path
from . import views

urlpatterns = [
    path('menus', views.menus,name='menu'),
]