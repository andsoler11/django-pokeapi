import requests

class ExternalAPIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_data(self, params=None):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(self.api_url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch data from the external API.")
        
    def set_api_url(self, api_url):
        self.api_url = api_url
    