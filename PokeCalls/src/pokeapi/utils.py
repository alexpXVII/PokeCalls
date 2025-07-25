import requests

def get_resource(endpoint: str, resource_id_or_name: str = None, params: dict = None):
    url = endpoint
    if resource_id_or_name:
        url = f"{endpoint}{resource_id_or_name}/"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()