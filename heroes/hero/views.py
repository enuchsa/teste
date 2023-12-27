import requests

from rest_framework.response import Response
from rest_framework.views import APIView


class HeroList(APIView):
    url = "http://gateway.marvel.com/v1/public/characters?ts=100&apikey=16e90537a937e7b409088e3f860ebab2&hash=107b7a9b68745b0157bb5e2def3130d8"
    
    def get(self, request, format=None):
        response = requests.get(self.url, verify=False)
        return Response({"1": 1})


class HeroDetails(APIView):

    def get(self, request, pk, format=None):
        return Response({"1": 1})
