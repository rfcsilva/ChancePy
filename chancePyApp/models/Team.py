from django.db import models

from .Country import Country
from .League import League


class Team(models.Model):
    external_id = models.IntegerField()
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    leagues = models.ManyToManyField(League)
