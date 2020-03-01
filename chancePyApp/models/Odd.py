from django.db import models

from .Game import Game


class Odd(models.Model):
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=25)
    value = models.FloatField()
    won = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)