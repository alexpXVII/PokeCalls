import pytest
from src.api_client import ApiClient

@pytest.fixture
def api_client():
    return ApiClient(base_url="https://api.example.com")

def test_get_request(mocker, api_client):
    mock_response = mocker.patch('src.api_client.requests.get')
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {"key": "value"}

    response = api_client.get("/endpoint")
    
    assert response.status_code == 200
    assert response.json() == {"key": "value"}
    mock_response.assert_called_once_with("https://api.example.com/endpoint")

def test_post_request(mocker, api_client):
    mock_response = mocker.patch('src.api_client.requests.post')
    mock_response.return_value.status_code = 201
    mock_response.return_value.json.return_value = {"key": "created"}

    response = api_client.post("/endpoint", data={"key": "value"})
    
    assert response.status_code == 201
    assert response.json() == {"key": "created"}
    mock_response.assert_called_once_with("https://api.example.com/endpoint", json={"key": "value"})

def test_put_request(mocker, api_client):
    mock_response = mocker.patch('src.api_client.requests.put')
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {"key": "updated"}

    response = api_client.put("/endpoint", data={"key": "value"})
    
    assert response.status_code == 200
    assert response.json() == {"key": "updated"}
    mock_response.assert_called_once_with("https://api.example.com/endpoint", json={"key": "value"})

def test_delete_request(mocker, api_client):
    mock_response = mocker.patch('src.api_client.requests.delete')
    mock_response.return_value.status_code = 204

    response = api_client.delete("/endpoint")
    
    assert response.status_code == 204
    mock_response.assert_called_once_with("https://api.example.com/endpoint")