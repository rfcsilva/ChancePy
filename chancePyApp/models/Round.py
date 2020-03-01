from django.db import models

from .League import League


class Round(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    number = models.IntegerField()