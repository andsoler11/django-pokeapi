from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from apps.berries.api_client import ExternalAPIClient
from apps.berries.models import Berrie
import requests


berries_url = '/allBerryStats'

class BerriesApiTests(TestCase):
    def setUp(self):
        # generate berries
        berrie =  {
                    'firmness': 'soft',
                    'flavors': [{'flavor': {'name': 'spicy',
                                            'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'},
                                'potency': 10},
                                {'flavor': {'name': 'dry',
                                            'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'},
                                'potency': 0},
                                {'flavor': {'name': 'sweet',
                                            'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'},
                                'potency': 0},
                                {'flavor': {'name': 'bitter',
                                            'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'},
                                'potency': 0},
                                {'flavor': {'name': 'sour',
                                            'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'},
                                'potency': 0}],
                    'growth_time': 3,
                    'id': 1,
                    'max_harvest': 5,
                    'name': 'cheri',
                    'natural_gift_power': 60,
                    'natural_gift_type': 'fire',
                    'size': 20,
                    'smoothness': 25,
                    'soil_dryness': 15
                }
        
        Berrie.objects.create(**berrie)
        
        self.client = APIClient()
        self.external_api_url = 'https://pokeapi.co/api/v2/berry'
        self.external_api_client = ExternalAPIClient(api_url=self.external_api_url)

        
    def test_api(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        assert 'Content-Type' in res
        
        res = res.json()
        assert 'berries_names' in res
        assert 'min_growth_time' in res
        assert 'median_growth_time' in res
        assert 'max_growth_time' in res
        assert 'variance_growth_time' in res
        assert 'mean_growth_time' in res
        assert 'frequency_growth_time' in res
  

    def test_names_count(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()

        assert len(res['berries_names']) == 1

    def test_external_api_call(self):
        res = self.external_api_client.get_data()
        
        assert 'count' in res

    def test_external_api_call_fail(self):
        self.external_api_client.set_api_url('https://pokeapi.co/api/v2/berry/0')
        with self.assertRaises(Exception):
            self.external_api_client.get_data()
            
    def test_names(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()
        
        assert res['berries_names'] == ['cheri']
        
    def test_min_growth_time(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()
        
        assert res['min_growth_time'] == 3
        
    def test_median_growth_time(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()
        
        assert res['median_growth_time'] == 3
        
    def test_max_growth_time(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()
        
        assert res['max_growth_time'] == 3

    def test_variance_growth_time(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()
        
        assert res['variance_growth_time'] == 0
        
    def test_mean_growth_time(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()
        
        assert res['mean_growth_time'] == 3
    
    def test_frequency_growth_time(self):
        res = self.client.get(berries_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = res.json()

        assert res['frequency_growth_time'] == {'3': 1}
