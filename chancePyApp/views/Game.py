from django.conf import settings
from django.http import HttpResponse
import time
from datetime import datetime

from chancePyApp.models import Game
from chancePyApp.views import Team

def load_all_games(request, id):
	leagues = League.objects.all()
	for league in leagues:
		for season in get_league_seasons(league.external_id):

			print(f"Getting events of {league.name} in season {season['strSeason']}")

			# Building HTTP request
			params = {'id': league.external_id, 's': season['strSeason']}
			events_json = http.GET(settings.EVENTS_LEAGUE_SEASON, params)['events']

			for event_json in events_json:
				if not is_in_DB(event_json['idEvent']):
					load_game(event_json, league)
					time.sleep(2)

	print('game_details')


def load_game(event_json, league):

	visited = Team.find_by_name(event_json['strHomeTeam'])
	visitors = Team.find_by_name(event_json['strAwayTeam'])

	# TODO: add overtime goals
	visited_goals = goals_by_half(event_json['strHomeGoalDetails'])
	visitors_goals = goals_by_half(event_json['strAwayGoalDetails'])

	game = Game(external_id=event_json['idEvent'],
				round_nr=event_json['intRound'],
				league=league,
				name=event_json['strEvent'],
				visited=visited,
				visitors=visitors,
				visited_goals= sum(visited_goals),
				visitors_goals=sum(visitors_goals), 
				visited_goals_half_time=visited_goals[0],
				visitors_goals_half_time=visitors_goals[0],
				externalFileName=event_json['strFilename'],
				visited_shots=event_json['intHomeShots'],
				visitors_shots=event_json['intAwayShots'],
				date=datetime.strptime(event_json['dateEvent'], "%Y-%m-%d")
	game.save()

def get_league_seasons(id):
	# Building HTTP request
	params = {'id': league.external_id}
	return http.GET(settings.LEAGUE_SEASONS_URL, params)['seasons']
	

def is_in_DB(id):
	return Game.objects.filter(external_id=id).count() > 0


def goals_by_half(total_goals_full_string):
	goals = [0, 0]
	splited_goal_string = map( lambda goal : goal.split("':")[0], away_goals.split(';')[:-1])
	for goal in splited_goal_string:
		if goal > 45:
			goal[0] = goals[0] + 1
		else:
			goals[1] = goals[1] + 1
	return goals