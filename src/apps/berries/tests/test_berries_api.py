from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from apps.berries.api_client import ExternalAPIClient
import requests


berries_url = '/allBerryStats'

class BerriesApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.external_api_url = 'https://pokeapi.co/api/v2/berry'
        self.external_api_client = ExternalAPIClient(api_url=self.external_api_url)

        
    def test_api(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        assert 'berries_names' in res.data
        assert 'min_growth_time' in res.data
        assert 'median_growth_time' in res.data
        assert 'max_growth_time' in res.data
        assert 'variance_growth_time' in res.data
        assert 'mean_growth_time' in res.data
        assert 'frequency_growth_time' in res.data
        assert 'Content-Type' in res

    def test_names_count(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        external_api_response = requests.get(self.external_api_url)
        external_api_data = external_api_response.json()
        total_count = external_api_data['count']

        assert len(res.data['berries_names']) == total_count

    def test_external_api_call(self):
        res = self.external_api_client.get_data()
        
        assert 'count' in res

    def test_external_api_call_fail(self):
        self.external_api_client.set_api_url('https://pokeapi.co/api/v2/berry/0')
        with self.assertRaises(Exception):
            self.external_api_client.get_data()
