from rest_framework.response import Response
from rest_framework.views import APIView


class GropuList(APIView):

    def get(self, request, format=None):

        return Response({"1": 1})

    def post(self, request, format=None):

        return Response({"1": 1})


class GroupDetails(APIView):

    def get(self, request, pk, format=None):
        return Response({"1": 1})

    def patch(self, request, pk, format=None):
        return Response({"1": 1})

    def put(self, request, pk, format=None):
        return Response({"1": 1})
