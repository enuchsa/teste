import requests

from rest_framework.response import Response
from rest_framework.views import APIView


class HeroList(APIView):

    def get(self, request, format=None):
        response = requests.get("http://gateway.marvel.com/v1/public/characters?ts=1&apikey=16e90537a937e7b409088e3f860ebab2&hash=74bbf5881022288b961e45977482d945")
        return Response({"1": 1})


class HeroDetails(APIView):

    def get(self, request, pk, format=None):
        return Response({"1": 1})
