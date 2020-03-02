import json

from django.conf import settings
from django.http import HttpResponse


def clean_leagues(request):
    soccer_leagues, handball_leagues, basketball_leagues, ice_hockey_leagues, volleyball_leagues = [], [], [], [], []
    if settings.LEAGUES:
        with open(settings.LEAGUES) as leagues_file:
            full_json = json.loads(leagues_file.read())
            n_leagues = 0
            for league in full_json['leagues']:
                n_leagues += 1
                if league['strSport'] == 'Soccer':
                    soccer_leagues.append(league)
                elif league['strSport'] == 'Handball':
                    handball_leagues.append(league)
                elif league['strSport'] == 'Basketball':
                    basketball_leagues.append(league)
                elif league['strSport'] == 'Volleyball':
                    volleyball_leagues.append(league)
                elif league['strSport'] == 'Ice Hockey':
                    ice_hockey_leagues.append(league)

    write_as_json('data/soccer', soccer_leagues)
    write_as_json('data/handball', handball_leagues)
    write_as_json('data/basket', basketball_leagues)
    write_as_json('data/voley', volleyball_leagues)
    write_as_json('data/hockey', ice_hockey_leagues)
    return HttpResponse('')


def write_as_json(file_name, data):
    with open(f'{file_name}.json', 'w') as f:
        json.dump(data, f)
    f.close()


def from_json(file_name):
    print(f'Reading json from {file_name} ...')
    with open(file_name) as file:
        data = json.load(file)
    file.close()
    return data
