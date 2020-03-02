import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import csv

from django.template import loader

from chancePyApp.models import Country


def countries_index(request):
    return JsonResponse(list(Country.objects.all().values('name', 'code')), safe=False)


def country_by_id(request, country_id):
    print(f'Sending data of {country_id}')
    country = Country.objects.get(pk=country_id)
    dict_country = model_to_dict(country)
    serialized_country = json.dumps(dict_country)
    return HttpResponse(serialized_country)


def load_countries(request):
    print('Listing...')

    if settings.COUNTRIES:
        with open(settings.COUNTRIES) as countries_file:
            csv_reader = csv.reader(countries_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    c = Country(name=row[0], code=row[1])
                    c.save()
                    print(f'name: {row[0]}, code: {row[1]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
    return HttpResponse(loader.get_template('loaded_countries.html').render())
