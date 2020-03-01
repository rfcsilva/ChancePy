from django.http import HttpResponse
from .league import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Swag")
