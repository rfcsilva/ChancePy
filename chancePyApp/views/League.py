from django.conf import settings
from django.http import HttpResponse

from chancePyApp.http import http
from chancePyApp.models import Country, League
from chancePyApp.utils import from_json


def league_index(request):
    return HttpResponse("Hello, world. You're at the polls index. League")


def load_leagues(request):
    if settings.LEAGUES_ARR:
        for league_path in settings.LEAGUES_ARR:
            for shallow_league in from_json(league_path):
                print('Printing shallow League')
                print(shallow_league)
                load_league(shallow_league)
    return HttpResponse('')


def load_league(shallow_league):
    country = None
    if settings.LEAGUE_LOOKUP_URL:
        params = {'id': shallow_league['idLeague']}
        print(params)
        data = http.GET(settings.LEAGUE_LOOKUP_URL, params)
        country_name = check_if_UK(data['strCountry'])
        country_query_set = Country.objects.filter(name=country_name)
        if country_query_set.count() == 1:
            country = country_query_set.first()
        league = League(external_id=data['idLeague'], sport=data['strSport'],
                        name=data['strLeague'], currentSeason=data['strCurrentSeason'],
                        country=country)
        print(league)


def check_if_UK(country_name):
    if country_name == ('England' or 'Scotland' or 'Northern Ireland'):
        return 'United Kingdom'
    else:
        return country_name
