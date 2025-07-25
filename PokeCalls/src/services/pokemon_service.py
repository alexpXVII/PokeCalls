from functools import lru_cache
from models.Pokemon import Pokemon
from pokeapi.core import get_pokemon

class PokemonService:
    @staticmethod
    @lru_cache(maxsize=128)
    def fetch_pokemon(pokemon_id_or_name):
        data = get_pokemon(pokemon_id_or_name)
        return Pokemon.from_json(data)