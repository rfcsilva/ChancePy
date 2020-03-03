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

	return HttpResponse('')