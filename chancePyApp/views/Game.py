from django.conf import settings
from django.http import HttpResponse


def load_all_games(request, id):
	leagues = League.objects.all()
	for league in leagues:
		for season in get_league_seasons(league.external_id):

			print(f"Getting events of {league.name} in season {season['strSeason']}")

			# Building HTTP request
			params = {'id': league.external_id, 's': season['strSeason']}
			events_json = http.GET(settings.EVENTS_LEAGUE_SEASON, params)['events']

			for event_json in events_json:


	print('game_details')


def get_league_seasons(id):
	# Building HTTP request
	params = {'id': league.external_id}
	return http.GET(settings.LEAGUE_SEASONS_URL, params)['seasons']
	