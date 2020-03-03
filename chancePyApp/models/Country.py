from django.db import models
import json


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name