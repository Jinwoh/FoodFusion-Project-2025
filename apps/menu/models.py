from django.db import models

# Create your models here.
class MenuCategoria(models.Model):
    id_menu_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'menu_categoria'
    def __str__(self):
        return self.nombre    

class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField()
    img_url = models.TextField(null=True)
    id_categoria = models.ForeignKey(MenuCategoria, on_delete=models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'menu'