from django.conf import settings
from django.http import HttpResponse
import time
from datetime import datetime

from chancePyApp.models import Game, League
from chancePyApp.views import find_team_by_name 

from chancePyApp.http import http

def load_all_games(request):
	leagues = League.objects.filter(sport='Soccer')
	for league in leagues:
		for season in get_league_seasons(league.external_id):

			print(f"Getting events of {league.name} in season {season['strSeason']}")

			# Building HTTP request
			params = {'id': league.external_id, 's': season['strSeason']}
			events_json = http.GET(settings.EVENTS_LEAGUE_SEASON, params)['events']

			for event_json in events_json:
				if not is_in_DB(event_json['idEvent']):
					print(f"Processing of {event_json['strEvent']} of season {season['strSeason']}")
					load_game(event_json, league)

	print('game_details')


def load_game(event_json, league):

	visited = find_team_by_name(event_json['strHomeTeam'])
	visitors = find_team_by_name(event_json['strAwayTeam'])

	goals = get_goals(event_json)

	game = Game(external_id=event_json['idEvent'],
				round_nr= event_json['intRound'] if event_json['intRound'] is not None else -1,
				league=league,
				name=event_json['strEvent'],
				visited=visited,
				visitors=visitors,
				visited_goals= sum(goals[0]),
				visitors_goals=sum(goals[1]), 
				visited_goals_half_time=goals[0][0],
				visitors_goals_half_time=goals[1][0],
				externalFileName=event_json['strFilename'],
				visited_shots=event_json['intHomeShots'] or -1,
				visitors_shots=event_json['intAwayShots'] or -1,
				date=datetime.strptime(event_json['dateEvent'], "%Y-%m-%d"))
	game.save()

def get_league_seasons(id):
	# Building HTTP request
	params = {'id': id}
	return http.GET(settings.LEAGUE_SEASONS_URL, params)['seasons']
	

def is_in_DB(id):
	return Game.objects.filter(external_id=id).count() > 0


def get_goals(event_json):
	# TODO: add overtime goals
	if event_json['strHomeGoalDetails'] is None or "":
		visited_goals = [int(event_json['intHomeScore']), 0]
	else:
		visited_goals = goals_by_half(event_json['strHomeGoalDetails'])

	if event_json['strAwayGoalDetails'] is None or "":
		visitors_goals = [int(event_json['intAwayScore']), 0]
	else:
		visitors_goals = goals_by_half(event_json['strAwayGoalDetails'])

	return [visited_goals, visitors_goals]	


def goals_by_half(total_goals_full_string):
	goals = [0, 0]
	splited_goal_string = map( lambda goal : goal.split("':")[0], total_goals_full_string.split(';')[:-1])
	for goal in map( lambda goal: int(goal), splited_goal_string):
		if goal > 45:
			goals[0] = goals[0] + 1
		else:
			goals[1] = goals[1] + 1
	return goals