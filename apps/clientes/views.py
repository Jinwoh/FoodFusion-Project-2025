from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página de clientes")

def mis_datos(request):
    return render(request, 'mis_datos.html')