from django.db import models

from .Player import Player
from .Round import Round
from .Team import Team


class Game(models.Model):
    external_id = models.IntegerField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    visited = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visited')
    visitors = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visitors')
    visited_goals = models.IntegerField()
    visited_goals_half_time = models.IntegerField()
    visitors_goals = models.IntegerField()
    visitors_goals_half_time = models.IntegerField()
    externalFileName = models.CharField(max_length=150)
    visited_shots = models.IntegerField()
    visitors_shots = models.IntegerField()
    date = models.DateField()
    visited_players = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='visited_players')
    visitors_players = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='visitors_players')