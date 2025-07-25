# Example class for the JSON returned by https://pokeapi.co/api/v2/pokemon/7
# filepath: c:\Github\PokeCalls\PokeCalls\PokeCalls\src\models\pokemon.py

from typing import List, Optional, Set
from types import SimpleNamespace
from .PokemonMove import PokemonMove

class PokemonAbility:
    def __init__(self, ability: dict, is_hidden: bool, slot: int):
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot

class PokemonType:
    def __init__(self, slot: int, type_: dict):
        self.slot = slot
        self.type = type_

# Example response from https://pokeapi.co/api/v2/pokemon/7/
# {
#   "id": 7,
#   "name": "squirtle",
#   "base_experience": 63,
#   "height": 5,
#   "is_default": true,
#   "order": 10,
#   "weight": 90,
#   "abilities": [
#     {
#       "is_hidden": false,
#       "slot": 1,
#       "ability": {"name": "torrent", "url": "..."}
#     },
#     ...
#   ],
#   "types": [
#     {
#       "slot": 1,
#       "type": {"name": "water", "url": "..."}
#     }
#   ],
#   "moves": [
#     {
#       "move": {"name": "mega-punch", "url": "..."},
#       "version_group_details": [...]
#     },
#     ...
#   ],
#   ...
# }
class Pokemon(SimpleNamespace):
    @classmethod
    def from_json(cls, data: dict):
        # Convert abilities and types to objects, moves to a set of PokemonMove
        abilities = [PokemonAbility(**a) for a in data.get("abilities", [])]
        types = [PokemonType(slot=t["slot"], type_=t["type"]) for t in data.get("types", [])]
        moves = []
        moves_list = set()
        for move in data.get("moves", []):
            new_move = PokemonMove.from_json(move['move'])
            moves.append(new_move)
            moves_list.add(new_move.name)
        # Use SimpleNamespace for all other fields
        ns = cls(**data)
        ns.abilities = abilities
        ns.types = types
        ns.moves = moves
        return ns