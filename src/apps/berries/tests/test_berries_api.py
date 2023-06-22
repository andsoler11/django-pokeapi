from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

berries_url = '/allBerryStats'

class BerriesApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
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