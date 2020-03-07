from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('league', views.league_index),
    path('league/count/', views.league_counting),

    # Teams endpoints
    path('teams/load', views.load_teams),

    # Countries endpoints
    path('countries/', views.countries_index),
    path('countries/<int:country_id>/', views.country_by_id, name='country_id'),
    path('countries/load', views.load_countries),
    path('dev', views.load_leagues),

    # Games endpoints
    path('games/load', views.load_all_games)
]
