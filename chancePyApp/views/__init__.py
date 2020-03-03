from .League import *
from .Country import *
from .Team import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Swag")
