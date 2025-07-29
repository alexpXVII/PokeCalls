import unittest
from unittest.mock import patch, MagicMock
from logic.game import Game

class TestGame(unittest.TestCase):
    @patch('logic.game.PokemonService')
    def test_guess_pokemon_match(self, mock_service):
        # Mock Pokémon objects
        mock_pokemon = MagicMock()
        mock_pokemon.name = "pikachu"
        mock_pokemon.height = 4
        mock_pokemon.weight = 60

        # Set up the service to return the mock Pokémon
        mock_service.fetch_pokemon.return_value = mock_pokemon

        game = Game("Ash")
        game.secret_pokemon = mock_pokemon  # Set secret to match

        result = game.guess_pokemon("pikachu")
        self.assertIn("Name: Match!", result)
        self.assertIn("Height: Match!", result)
        self.assertIn("Weight: Match!", result)

    @patch('logic.game.PokemonService')
    def test_guess_pokemon_higher_lower(self, mock_service):
        mock_pokemon1 = MagicMock()
        mock_pokemon1.name = "bulbasaur"
        mock_pokemon1.height = 7
        mock_pokemon1.weight = 80

        mock_pokemon2 = MagicMock()
        mock_pokemon2.name = "charmander"
        mock_pokemon2.height = 5
        mock_pokemon2.weight = 90

        mock_service.fetch_pokemon.return_value = mock_pokemon1

        game = Game("Ash")
        game.secret_pokemon = mock_pokemon2

        result = game.guess_pokemon("bulbasaur")
        self.assertIn("Name: bulbasaur vs charmander", result)
        self.assertIn("Height: Higher", result)
        self.assertIn("Weight: Lower", result)

if __name__ == "__main__":
    unittest.main()