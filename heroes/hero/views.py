import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from heroes.hero.serializers import HeroesResponse


class HeroList(APIView):
    URL = "http://gateway.marvel.com/v1/public/characters"

    def get(self, request, format=None):
        response = requests.get(
            self.URL,
            params={
                "ts": "100",
                "apikey": "16e90537a937e7b409088e3f860ebab2",
                "hash": "107b7a9b68745b0157bb5e2def3130d8",
                "offset": 0,
                "limit": 100,
            },
            verify=False
        )

        heroes_list = HeroesResponse(**response.json())

        return Response(heroes_list.model_dump())


class HeroDetails(APIView):

    def get(self, request, pk, format=None):
        return Response({"1": 1})
