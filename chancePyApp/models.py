from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)


class League(models.Model):
    external_id = models.IntegerField()
    sport = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    currentSeason = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Team(models.Model):
    external_id = models.IntegerField()
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Player(models.Model):
    external_id = models.IntegerField()
    name = models.CharField(max_length=100)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    birthday = models.DateField()
    played_at = models.ManyToManyField(Team)


class Round(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    number = models.IntegerField()


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


class Odd(models.Model):
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=25)
    value = models.FloatField()
    won = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
