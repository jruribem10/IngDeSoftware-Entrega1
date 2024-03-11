from django.db import models

# Create your models here.

class Cerveza(models.Model):
    name = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)  # Campo correspondiente a 'tipo' en el formulario
    alcohol = models.FloatField()  # Campo correspondiente a 'alcohol' en el formulario
    color = models.CharField(max_length=255)  # Campo correspondiente a 'color' en el formulario
    amargor = models.CharField(max_length=255)  # Campo correspondiente a 'amargor' en el formulario
    descripcion = models.TextField()  # Campo correspondiente a 'descripcion' en el formulario
    price = models.FloatField()  # Campo correspondiente a 'precio' en el formulario
    casa = models.CharField(max_length=255)  # Campo correspondiente a 'casa' en el formulario
    image = models.ImageField(upload_to='threemanPubimagenes')