import unittest
from unittest.mock import patch, MagicMock
from logic.game import Game
from models.pokemon import Pokemon
from models.move import Move

class TestGame(unittest.TestCase):
    @patch('services.pokemon_service.PokemonService.fetch_pokemon')
    def test_guess_pokemon_match(self, mock_fetch_pokemon):
        # Mock Pokémon object
        mock_pokemon = MagicMock(spec=Pokemon)
        mock_pokemon.name = "pikachu"
        mock_pokemon.height = 4
        mock_pokemon.weight = 60

        mock_fetch_pokemon.return_value = mock_pokemon

        game = Game("Ash")
        game.secret_pokemon = mock_pokemon  # Set secret to match

        result = game.guess_pokemon("pikachu")
        self.assertIn("Name: Match!", result)
        self.assertIn("Height: Match!", result)
        self.assertIn("Weight: Match!", result)

    @patch('services.pokemon_service.PokemonService.fetch_pokemon')
    def test_guess_pokemon_higher_lower(self, mock_fetch_pokemon):
        mock_pokemon1 = MagicMock(spec=Pokemon)
        mock_pokemon1.name = "bulbasaur"
        mock_pokemon1.height = 7
        mock_pokemon1.weight = 80

        mock_pokemon2 = MagicMock(spec=Pokemon)
        mock_pokemon2.name = "charmander"
        mock_pokemon2.height = 5
        mock_pokemon2.weight = 90

        mock_fetch_pokemon.return_value = mock_pokemon1

        game = Game("Ash")
        game.secret_pokemon = mock_pokemon2

        result = game.guess_pokemon("bulbasaur")
        self.assertIn("Name: Wrong", result[0])  # compare_values returns "Wrong" for name mismatch
        self.assertIn("Height: Higher", result[1])
        self.assertIn("Weight: Lower", result[2])

    @patch('services.move_service.MoveService.fetch_move')
    def test_guess_move_match(self, mock_fetch_move):
        mock_move = MagicMock(spec=Move)
        mock_move.type = {"name": "electric"}
        mock_move.damage_class = {"name": "special"}
        mock_move.power = 90
        mock_move.pp = 15
        mock_move.accuracy = 100
        mock_move.target = {"name": "selected-pokemon"}
        mock_move.effect_entries = [{"effect": "May paralyze."}]

        mock_fetch_move.return_value = mock_move

        game = Game("Ash")
        game.secret_move = mock_move

        result = game.guess_move("thunderbolt", game.secret_move)
        self.assertIn("Type: Match!", result)
        self.assertIn("Category: Match!", result)
        self.assertIn("Power: Match!", result)
        self.assertIn("PP: Match!", result)
        self.assertIn("Accuracy: Match!", result)
        self.assertIn("Target: Match!", result)
        self.assertIn("Has Effect: Match!", result)

if __name__ == "__main__":
    unittest.main()