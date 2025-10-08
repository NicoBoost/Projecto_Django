from django.db import models

# Create your models here.
class myapp(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(myapp, on_delete=models.CASCADE)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre