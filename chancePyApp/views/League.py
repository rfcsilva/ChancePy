from django.conf import settings
from django.http import HttpResponse

from chancePyApp.http import http
from chancePyApp.models import Country, League
from chancePyApp.utils import from_json
import time


def league_index(request):
    return HttpResponse("Hello, world. You're at the polls index. League")


def load_leagues(request):
    if settings.LEAGUES_ARR:
        for league_path in settings.LEAGUES_ARR:
            for shallow_league in from_json(league_path):
                print('#########################')
                print('Printing shallow League')
                print(shallow_league)
                load_league(shallow_league)

                time.sleep(1.5)
    return HttpResponse('')


def load_league(shallow_league):
    country = None
    if settings.LEAGUE_LOOKUP_URL:
        params = {'id': shallow_league['idLeague']}
        
        #TODO: If data lenght > 1
        data = http.GET(settings.LEAGUE_LOOKUP_URL, params)['leagues'][0]

        country_name = check_if_UK(data['strCountry'])
        
        print(f"Old Country Name: {data['strCountry']}")
        print(f"New Country Name: {country_name}")
        country_query_set = Country.objects.filter(name=country_name)
        if country_query_set.count() == 1:
            country = country_query_set.first()
        
        print(country)
        league = League(external_id=data['idLeague'], sport=data['strSport'],
                        name=data['strLeague'], currentSeason=data['strCurrentSeason'],
                        country=country)
        print(league)


def check_if_UK(country_name):
    if country_name in {'England', 'Scotland', 'Northern Ireland'}:
        return 'United Kingdom'
    else:
        return country_name
