from rest_framework import viewsets
from rest_framework.response import Response

class BerriesViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Hello, world!"}, status=200)