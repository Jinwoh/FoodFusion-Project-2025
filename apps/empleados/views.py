from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def es_empleado(user):
    return user.is_staff