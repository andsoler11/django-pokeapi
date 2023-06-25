from django.shortcuts import render
from rest_framework import viewsets
import pandas as pd
from django.http import JsonResponse
from apps.berries.models import Berrie
from apps.berries.serializers import BerrieSerializer

class BerriesViewSet(viewsets.ViewSet):
    """ViewSet for the berries API."""
    queryset = Berrie.objects.all()
    serializer_class = BerrieSerializer
    
    def list(self, request):
        """GET /allBerryStats, return a JSON response with the following data:
            - berries_names: list of all berries names
            - min_growth_time: minimum growth time
            - median_growth_time: median growth time
            - max_growth_time: maximum growth time
            - variance_growth_time: variance of growth time
            - mean_growth_time: mean of growth time
            - frequency_growth_time: frequency of growth time
        """
        
        # get all berries from the database
        serializer = self.serializer_class(self.queryset, many=True)
        
        # convert the berries to a list of dictionaries
        berries = list(serializer.data)

        # create a pandas dataframe from the list of dictionaries
        df = pd.DataFrame.from_dict(berries)
        
        output = {
            'berries_names': df['name'].to_list(),
            "min_growth_time": int(df['growth_time'].min()),
            "median_growth_time": float(df['growth_time'].median()),
            "max_growth_time": int(df['growth_time'].max()),
            "variance_growth_time": float(df['growth_time'].var()) if len(df['growth_time']) > 1 else 0,
            "mean_growth_time": float(df['growth_time'].mean()),
            "frequency_growth_time": df['growth_time'].value_counts().to_dict()
        }
        
        response = JsonResponse(output, json_dumps_params={'indent': 4})
        response['Content-Type'] = 'application/json'
        return response


def display_histogram(request):
    """GET /histogram, render the histogram template"""

    return render(request, 'histogram.html')