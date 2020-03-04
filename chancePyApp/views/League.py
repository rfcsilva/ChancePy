from django.conf import settings
from django.http import HttpResponse, JsonResponse

from chancePyApp.http import http
from chancePyApp.models import Country, League
from chancePyApp.utils import from_json
import time


def league_index(request):
    return JsonResponse(list(League.objects.all().values('name')), safe=False)


def league_counting(request):
    n_soccer = League.objects.filter(sport='Soccer').count()
    n_handball = League.objects.filter(sport='Handball').count()
    n_basketball = League.objects.filter(sport='Basketball').count()
    n_hockey = League.objects.filter(sport='Ice Hockey').count()
    n_voley = League.objects.filter(sport='Volleyball').count()
    stats = {'n_soccer': n_soccer, 'n_handball': n_handball, 'n_basketball': n_basketball, 'n_hockey': n_hockey, 'n_voley': n_voley}
    return JsonResponse(stats, safe=False)


def league_details(request):
    print('league_details')


def league_round(request, round):
    print('league_round')


def load_leagues(request):
    if settings.LEAGUES_ARR:
        for league_path in settings.LEAGUES_ARR:
            for shallow_league in from_json(league_path):
                if not is_in_DB(shallow_league['idLeague']):
                    load_league(shallow_league)
                    time.sleep(2)
    return HttpResponse('')


def load_league(shallow_league):
    country = None
    if settings.LEAGUE_LOOKUP_URL:
        params = {'id': shallow_league['idLeague']}
            
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
            league.save()            

def fix_country_name(country_name):

    print(f'Fixing {country_name}')
    if country_name in {'England', 'Scotland', 'Wales','Northern Ireland', 'UK', 'GB'}:
        return 'United Kingdom'
    elif country_name in {"Holland", "The Netherlands"}:
        return 'Netherlands'
    elif country_name == "USA":
        return 'United States'
    elif country_name == "Russia":
        return 'Russian Federation'
    elif country_name == "Venezuela":
        return "Venezuela, Bolivarian Republic of"
    elif country_name == "Bosnia":
        return 'Bosnia and Herzegovina'
    elif country_name == "Macedonia":
        return "Macedonia, the Former Yugoslav Republic of"
    elif country_name == "Moldova":
        return "Moldova, Republic of"
    elif country_name == "Saudi-Arabia":
        return "Saudi Arabia"
    elif country_name == "UAE":
        return "United Arab Emirates"
    elif country_name == "Bolivia":
        return "Bolivia, Plurinational State of"
    elif country_name == "South Korea":
        return "Korea, Republic of"
    elif country_name == "Iran":
        return "Iran, Islamic Republic of"
    else:
        return country_name

def is_in_DB(code):
    return League.objects.filter(external_id=code).count() > 0