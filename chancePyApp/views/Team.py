from django.conf import settings
from django.http import HttpResponse, JsonResponse

from chancePyApp.http import http
from chancePyApp.models import Country, League, Team
from chancePyApp.utils import from_json
import time


def load_teams(request):
	leagues = League.objects.all()
	for league in leagues:
		print(f'Loading teams of {league.name}')

		# Building HTTP request
		params = {'id': league.external_id}
		teams_json = http.GET(settings.TEAMS_BY_LEAGUE_URL, params)['teams']
		
		if teams_json is not None and len(teams_json) > 0:
			for team_json in teams_json:
				if not is_in_DB(team_json['idTeam']):
					load_team(team_json, league, league.country)
	return HttpResponse('')

def load_team(team_json, league, country):
	print(f"Processing {team_json['strTeam']}")
	team = Team(external_id=team_json['idTeam'], name=team_json['strTeam'],
				country=country)
	team.save()

	# Add many-to-many relation
	team.leagues.add(league)
	print(team)

def is_in_DB(code):
    return Team.objects.filter(external_id=code).count() > 0