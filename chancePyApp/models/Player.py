from django.db import models

from .Country import Country
from .Team import Team


class Player(models.Model):
    external_id = models.IntegerField()
    name = models.CharField(max_length=100)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    birthday = models.DateField()
    played_at = models.ManyToManyField(Team)