from django.db import models


class Catalogpokemon(models.Model):
    generacion = models.CharField(max_length=30)
    cantidad = models.IntegerField(default=0)

