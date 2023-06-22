from rest_framework import viewsets
from rest_framework.response import Response
from .api_client import ExternalAPIClient

class BerriesViewSet(viewsets.ViewSet):
    api_url = 'https://pokeapi.co/api/v2/berry'

    def list(self, request):
            api_client = ExternalAPIClient(api_url=self.api_url)

            try:
                data = api_client.get_data()
            except Exception as e:
                return Response({"error": str(e)}, status=500)

            return Response(data, status=200)