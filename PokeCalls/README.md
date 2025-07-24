# REST API Helper

## Overview
The REST API Helper is a Python library designed to simplify the process of making REST API calls. It provides an easy-to-use `ApiClient` class that supports various HTTP methods, along with utility functions to assist with API interactions.

## Features
- Simple and intuitive API for making HTTP requests.
- Supports GET, POST, PUT, and DELETE methods.
- Utility functions for handling responses and building URLs.

## Installation
To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage
Here is a basic example of how to use the `ApiClient` class:

```python
from src.api_client import ApiClient

# Create an instance of ApiClient
client = ApiClient(base_url="https://api.example.com")

# Make a GET request
response = client.get("/endpoint")
print(response)

# Make a POST request
data = {"key": "value"}
response = client.post("/endpoint", json=data)
print(response)
```

## Running Tests
To run the unit tests for the `ApiClient`, use the following command:

```
pytest tests/test_api_client.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.