import json
import pytest
from unittest.mock import patch
from django.urls import reverse

# Mark all tests in this module as needing database access
pytestmark = pytest.mark.django_db

@pytest.fixture
def client():
    """A Django test client instance."""
    from django.test import Client
    return Client()

@pytest.fixture
def guess_pokemon_url():
    """URL for the guess-pokemon endpoint."""
    return reverse('guess-pokemon')

@pytest.fixture
def guess_move_url():
    """URL for the guess-move endpoint."""
    return reverse('guess-move')

@patch('api.views.GAME_INSTANCE')
def test_guess_pokemon_success(mock_game_instance, client, guess_pokemon_url):
    """Test successful Pokémon guess."""
    mock_game_instance.guess_pokemon.return_value = ["Name: Match!", "Height: Lower"]
    
    response = client.post(
        guess_pokemon_url,
        data=json.dumps({'guess': 'pikachu'}),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    assert response.json() == {'results': ["Name: Match!", "Height: Lower"]}
    mock_game_instance.guess_pokemon.assert_called_once_with('pikachu')

@patch('api.views.GAME_INSTANCE')
def test_guess_pokemon_not_found(mock_game_instance, client, guess_pokemon_url):
    """Test Pokémon guess when the Pokémon is not found."""
    mock_game_instance.guess_pokemon.return_value = None
    
    response = client.post(
        guess_pokemon_url,
        data=json.dumps({'guess': 'notapokemon'}),
        content_type='application/json'
    )
    
    assert response.status_code == 404
    assert 'error' in response.json()

def test_guess_pokemon_bad_request_no_guess(client, guess_pokemon_url):
    """Test Pokémon guess with missing 'guess' field."""
    response = client.post(
        guess_pokemon_url,
        data=json.dumps({'wrong_key': 'pikachu'}),
        content_type='application/json'
    )
    assert response.status_code == 400

def test_guess_pokemon_wrong_method(client, guess_pokemon_url):
    """Test using a method other than POST for Pokémon guess."""
    response = client.get(guess_pokemon_url)
    assert response.status_code == 400

@patch('api.views.GAME_INSTANCE')
def test_guess_move_success(mock_game_instance, client, guess_move_url):
    """Test successful move guess."""
    mock_game_instance.guess_move.return_value = ["Type: Match!", "Power: Higher"]
    
    response = client.post(
        guess_move_url,
        data=json.dumps({'guess': 'thunderbolt'}),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    assert response.json() == {'results': ["Type: Match!", "Power: Higher"]}
    mock_game_instance.guess_move.assert_called_once_with('thunderbolt', mock_game_instance.secret_move)

@patch('api.views.GAME_INSTANCE')
def test_guess_move_not_found(mock_game_instance, client, guess_move_url):
    """Test move guess when the move is not found."""
    mock_game_instance.guess_move.return_value = None
    
    response = client.post(
        guess_move_url,
        data=json.dumps({'guess': 'notamove'}),
        content_type='application/json'
    )
    
    assert response.status_code == 404
    assert 'error' in response.json()

def test_guess_move_bad_request_invalid_json(client, guess_move_url):
    """Test move guess with invalid JSON."""
    response = client.post(
        guess_move_url,
        data="this is not json",
        content_type='application/json'
    )
    assert response.status_code == 400