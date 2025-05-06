from django.db import models
from clientes.models import Cliente



class CategoriaMenu(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaMenu, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.precio} Gs"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre_apellido}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.menu.nombre} x{self.cantidad} (Pedido #{self.pedido.id})"