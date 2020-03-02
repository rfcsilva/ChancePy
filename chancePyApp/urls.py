from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('league', views.league_index),

    # Countries endpoints
    path('countries/', views.countries_index),
    path('countries/<int:country_id>/', views.country_by_id, name='country_id'),
    path('countries/load', views.load),
]
