from datetime import date
import random
from typing import List, Optional

from config import MAX_POKEMON_ID, MAX_MOVE_ID
from services.pokemon_service import PokemonService
from services.move_service import MoveService
from models.pokemon import Pokemon
from models.move import Move
from logic.comparisons import compare_pokemon, compare_moves


class Game:
    def __init__(self, player_name: str):
        self.player_name: str = player_name
        self.secret_pokemon: Optional[Pokemon] = self.get_daily_random_pokemon()
        self.current_pokemon: Optional[Pokemon] = None
        self.secret_move: Optional[Move] = self.get_daily_random_move()


    def guess_pokemon(self, pokemon_id_or_name: str) -> Optional[List[str]]:
        try:
            self.current_pokemon = PokemonService.fetch_pokemon(pokemon_id_or_name)
            return compare_pokemon(self.current_pokemon, self.secret_pokemon)
        except Exception as e:
            print(f"Error fetching Pokémon data: {e}")
            return None

    def guess_move(self, move_id_or_name: str, secret_move: Move) -> Optional[List[str]]:
        """
        Compares a guessed move to a secret move and returns a list of comparison results.
        """
        try:
            move_name = move_id_or_name.split(" ")
            guessed_move = MoveService.fetch_move('-'.join(move_name))
            return compare_moves(guessed_move, secret_move)
        except Exception as e:
            print(f"Error fetching Move data: {e}")
            return None

    @staticmethod
    def get_daily_random_pokemon() -> Pokemon:
        today = date.today().strftime("%Y%m%d")
        random.seed(today)
        pokemon_id = random.randint(1, MAX_POKEMON_ID)
        return PokemonService.fetch_pokemon(pokemon_id)
    
    @staticmethod
    def get_daily_random_move() -> Move:
        today = date.today().strftime("%Y%m%d")
        random.seed(today)
        move_id = random.randint(1, MAX_MOVE_ID)
        return MoveService.fetch_move(move_id)