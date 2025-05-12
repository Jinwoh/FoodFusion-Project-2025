from django.db import models

# Create your models here.
class MenuCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'menu_categoria'
    def __str__(self):
        return f" {self.id}  {self.nombre} "    

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField()
    img_url = models.TextField(null=True)
    menu_categoria_id = models.ForeignKey(MenuCategoria, on_delete=models.DO_NOTHING, db_column='menu_categoria_id')

    class Meta:
        managed = False
        db_table = 'menu'