from functools import lru_cache
from models.move import Move
from pokeapi.core import get_move

class MoveService:
    @staticmethod
    @lru_cache(maxsize=128)
    def fetch_move(move_id_or_name):
        data = get_move(move_id_or_name)
        return Move.from_json(data)