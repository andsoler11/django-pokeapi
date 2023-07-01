from django.core.management.base import BaseCommand
from apps.berries.api_client import ExternalAPIClient
from apps.berries.models import Berrie


class Command(BaseCommand):
    help = 'Import the berries from the poke api'
    api_url = 'https://pokeapi.co/api/v2/berry'

    def handle(self, *args, **options):
        api_client = ExternalAPIClient(api_url=self.api_url)
        
        try:
            data = api_client.get_data()
        except Exception as e:
            raise e
        
        # get the total count of berries so we can iterate over them
        total_count = data['count']
        
        for i in range(1, total_count + 1):
            # set the api url to the current berry and get the data
            api_client.set_api_url(f'https://pokeapi.co/api/v2/berry/{i}')
            try:
                response = api_client.get_data()
            except Exception as e:
                raise e

            Berrie.objects.update_or_create(
                id=response['id'],
                name=response['name'],
                growth_time=response['growth_time'],
                max_harvest=response['max_harvest'],
                natural_gift_power=response['natural_gift_power'],
                size=response['size'],
                smoothness=response['smoothness'],
                soil_dryness=response['soil_dryness'],
                firmness=response['firmness']['name'],
                flavors=response['flavors'],
                natural_gift_type=response['natural_gift_type']['name'],
            )
                
        self.stdout.write(self.style.SUCCESS('Successfully imported berries'))
            
        
        