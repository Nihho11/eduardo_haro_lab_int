from django.db import models


class Pokemon(models.Model):
    nombre_pokemon = models.CharField(max_length=40)
    numero = models.IntegerField()
    generacion = models.IntegerField()
    tipo = models.CharField(max_length=20)
