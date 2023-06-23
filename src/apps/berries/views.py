from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .api_client import ExternalAPIClient
from django.core.cache import cache
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class BerriesViewSet(viewsets.ViewSet):
    api_url = 'https://pokeapi.co/api/v2/berry'

    def list(self, request):
        result_list = cache.get('berries')
        if not result_list:
            api_client = ExternalAPIClient(api_url=self.api_url)

            try:
                data = api_client.get_data()
            except Exception as e:
                return Response({"error": str(e)}, status=500)

            total_count = data['count']
            result_list = []
            for i in range(1, total_count + 1):
                api_client.set_api_url(f'https://pokeapi.co/api/v2/berry/{i}')
                response = api_client.get_data()

                result_list.append({
                    'name': response['name'],
                    'growth_time': response['growth_time']
                })

            cache.set('berries', result_list, 60*60*24)

        df = pd.DataFrame.from_dict(result_list)

        output = {
            'berries_names': df['name'].to_list(),
            "min_growth_time": df['growth_time'].astype(int).min(),
            "median_growth_time": df['growth_time'].astype(float).median(),
            "max_growth_time": df['growth_time'].astype(int).max(),
            "variance_growth_time": df['growth_time'].astype(float).var(),
            "mean_growth_time": df['growth_time'].astype(float).mean(),
            "frequency_growth_time": df['growth_time'].value_counts().to_dict()
        }


        plt.hist(df['growth_time'].astype(float), bins='auto')
        plt.xlabel('Growth Time')
        plt.ylabel('Frequency')
        plt.title('Berry Growth Time Histogram')
        plt.savefig('static/images/histogram.png')
        plt.close()

        response = Response(output, status=200)
        response['Content-Type'] = 'application/json'

        return response

def display_histogram(request):
    return render(request, 'histogram.html')