import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(self.build_url(endpoint), params=params)
        return self.handle_response(response)

    def post(self, endpoint, data=None):
        response = requests.post(self.build_url(endpoint), json=data)
        return self.handle_response(response)

    def put(self, endpoint, data=None):
        response = requests.put(self.build_url(endpoint), json=data)
        return self.handle_response(response)

    def delete(self, endpoint):
        response = requests.delete(self.build_url(endpoint))
        return self.handle_response(response)

    def build_url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()