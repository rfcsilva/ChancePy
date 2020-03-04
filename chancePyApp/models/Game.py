from django.db import models

from .Player import Player
from .Team import Team
from .League import League


class Game(models.Model):
    external_id = models.IntegerField(unique=True)
    round_nr = models.IntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE, default=0)
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
   # visited_players = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='visited_players')
   # visitors_players = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='visitors_players')