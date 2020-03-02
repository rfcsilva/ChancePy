from django.db import models

from .Country import Country


class League(models.Model):
    external_id = models.IntegerField(unique=True)
    sport = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    currentSeason = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)