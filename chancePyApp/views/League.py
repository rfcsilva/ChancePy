from django.http import HttpResponse


def league_index(request):
    return HttpResponse("Hello, world. You're at the polls index. League")