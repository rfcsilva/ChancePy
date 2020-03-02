import json

from django.conf import settings
from django.http import HttpResponse

from chancePyApp.http import http
from chancePyApp.models import League
from chancePyApp.utils import from_json
from chancePyApp.models.Country import Country


def league_index(request):
    return HttpResponse("Hello, world. You're at the polls index. League")


def load_leagues(request):
    if settings.LEAGUES_ARR:
        for league_path in settings.LEAGUES_ARR:
            for shallow_league in from_json(league_path):
                load_league(shallow_league)
    return HttpResponse('')


def load_league(shallow_league):
    if settings.LEAGUE_LOOKUP_URL:
        params = {'id': shallow_league['idLeague']}
        data = http.GET(settings.LEAGUE_LOOKUP_URL, params)
        if data['strCountry'] == ('England' or 'Scotland' or 'Northern Ireland'):
            country_name = 'United Kingdom'
        else:
            country_name = data['strCountry']
