from django.core.management.base import BaseCommand
from apps.berries.api_client import ExternalAPIClient
from apps.berries.models import Berrie
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

class Command(BaseCommand):
    help = 'Generate the histogram png image'

    def handle(self, *args, **options):
        berries = Berrie.objects.all()
        berries_dict = list(berries.values())
        
        # create a pandas dataframe from the list of dictionaries
        df = pd.DataFrame.from_dict(berries_dict)
            
        # create the histogram
        plt.hist(df['growth_time'].astype(float), bins='auto')
        plt.xlabel('Growth Time')
        plt.ylabel('Frequency')
        plt.title('Berry Growth Time Histogram')
        plt.savefig('static/images/histogram.png')
        plt.close()

        self.stdout.write(self.style.SUCCESS('Successfully generated or updated histogram'))
        
        