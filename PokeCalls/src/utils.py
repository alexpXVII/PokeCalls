def handle_response(response):
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise Exception("Resource not found")
    elif response.status_code == 500:
        raise Exception("Server error")
    else:
        raise Exception(f"Unexpected error: {response.status_code}")

def build_url(base_url, endpoint, params=None):
    url = f"{base_url}/{endpoint}"
    if params:
        url += "?" + "&".join(f"{key}={value}" for key, value in params.items())
    return url