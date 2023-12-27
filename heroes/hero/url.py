from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from heroes.hero.views import HeroDetails, HeroList

url_heroes = [
    path('herois/', HeroList.as_view()),
    path('herois/<int:pk>/', HeroDetails.as_view()),
]

url_heroes = format_suffix_patterns(url_heroes)
