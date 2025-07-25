from datetime import date
import random

from services.pokemon_service import PokemonService
from config import MAX_POKEMON_ID


class Game:
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.secret_pokemon = self.get_daily_random_pokemon()
        self.current_pokemon = None

    def guess_pokemon(self, pokemon_id_or_name: str):
        try:
            self.current_pokemon = PokemonService.fetch_pokemon(pokemon_id_or_name)
            return self._compare_pokemon(self.current_pokemon, self.secret_pokemon)
        except Exception as e:
            print(f"Error fetching Pokémon data: {e}")
            return False
    
    @staticmethod
    def _compare_value(val1, val2):
        if val1 == val2:
            return "Match!"
        return "Higher" if val1 > val2 else "Lower"

    def _compare_pokemon(self, pokemon1, pokemon2):
        results = []
        # Name comparison
        if pokemon1.name == pokemon2.name:
            results.append("Name: Match!")
        else:
            results.append(f"Name: {pokemon1.name} vs {pokemon2.name}")

        # Height and Weight comparison using helper
        results.append(f"Height: {self._compare_value(pokemon1.height, pokemon2.height)}")
        results.append(f"Weight: {self._compare_value(pokemon1.weight, pokemon2.weight)}")

        return results
    
    @staticmethod
    def get_daily_random_pokemon():
        today = date.today().strftime("%Y%m%d")
        random.seed(today)
        pokemon_id = random.randint(1, MAX_POKEMON_ID)
        return PokemonService.fetch_pokemon(pokemon_id)