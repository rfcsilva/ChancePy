from .League import *
from .Country import *
from .Team import *
from .Game import load_all_games

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Swag")
