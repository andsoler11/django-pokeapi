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
    """ViewSet for the berries API."""

    # set the poke api url
    api_url = 'https://pokeapi.co/api/v2/berry'

    def list(self, request):
        """GET /allBerryStats"""

        # check if the data is in the cache
        result_list = cache.get('berries')
        if not result_list:
            # if not, get the data from the api
            api_client = ExternalAPIClient(api_url=self.api_url)
            try:
                data = api_client.get_data()
            except Exception as e:
                return Response({"error": str(e)}, status=500)

            # get the total count of berries so we can iterate over them
            total_count = data['count']
            # create an empty list to store the results
            result_list = []
            for i in range(1, total_count + 1):
                # set the api url to the current berry and get the data
                api_client.set_api_url(f'https://pokeapi.co/api/v2/berry/{i}')
                try:
                    response = api_client.get_data()
                except Exception as e:
                    return Response({"error": str(e)}, status=500)

                # append the data to the result list
                result_list.append({
                    'name': response['name'],
                    'growth_time': response['growth_time']
                })

            # set the data in the cache for 24 hours
            cache.set('berries', result_list, 60*60*24)

        # create a dataframe from the result list
        df = pd.DataFrame.from_dict(result_list)

        # create the output dictionary
        output = {
            'berries_names': df['name'].to_list(),
            "min_growth_time": df['growth_time'].astype(int).min(),
            "median_growth_time": df['growth_time'].astype(float).median(),
            "max_growth_time": df['growth_time'].astype(int).max(),
            "variance_growth_time": df['growth_time'].astype(float).var(),
            "mean_growth_time": df['growth_time'].astype(float).mean(),
            "frequency_growth_time": df['growth_time'].value_counts().to_dict()
        }

        # create the histogram image, or update it if it already exists
        plt.hist(df['growth_time'].astype(float), bins='auto')
        plt.xlabel('Growth Time')
        plt.ylabel('Frequency')
        plt.title('Berry Growth Time Histogram')
        plt.savefig('static/images/histogram.png')
        plt.close()

        # return the output as a json response with the content type set to json
        response = Response(output, status=200)
        response['Content-Type'] = 'application/json'

        return response

def display_histogram(request):
    """GET /histogram, render the histogram template"""

    return render(request, 'histogram.html')