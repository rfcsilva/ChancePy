from django.conf import settings
from django.http import HttpResponse

from chancePyApp.http import http
from chancePyApp.models import Country, League
from chancePyApp.utils import from_json
import time


def league_index(request):
    return HttpResponse("Hello, world. You're at the polls index. League")


def league_details(request):
    print('league_details')


def league_round(request, round):
    print('league_round')


def load_leagues(request):
    if settings.LEAGUES_ARR:
        for league_path in settings.LEAGUES_ARR:
            for shallow_league in from_json(league_path):
                #shallow_league = '1'
                print('#########################')
                print(f'Printing shallow League {shallow_league}')
                load_league(shallow_league)
                time.sleep(2)

    return HttpResponse('')


def load_league(shallow_league):
    country = None
    if settings.LEAGUE_LOOKUP_URL:
        params = {'id': shallow_league['idLeague']}
        #params = {'id': 4624}
        
        #TODO: If data lenght > 1
        data = http.GET(settings.LEAGUE_LOOKUP_URL, params)['leagues'][0]

        country_name = fix_country_name(data['strCountry'])
        
        #TODO: fix world cup
        if country_name not in {"Worldwide", "International", "Europe"}:
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
            

def fix_country_name(country_name):

    print(f'Fixing {country_name}')
    if country_name in {'England', 'Scotland', 'Wales','Northern Ireland', 'UK'}:
        return 'United Kingdom'
    elif country_name == "Holland":
        return 'Netherlands'
    elif country_name == "USA":
        return 'United States'
    elif country_name == "Russia":
        return 'Russian Federation'
    elif country_name == "Venezuela":
        return "Venezuela, Bolivarian Republic of"
    elif country_name == "Bosnia":
        return 'Bosnia and Herzegovina'
    else:
        return country_name
