# Example class for the JSON returned by https://pokeapi.co/api/v2/pokemon/7
# filepath: c:\Github\PokeCalls\PokeCalls\PokeCalls\src\pokemon.py

from typing import List, Optional, Set
from types import SimpleNamespace
from PokemonMove import PokemonMove

class PokemonAbility:
    def __init__(self, ability: dict, is_hidden: bool, slot: int):
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot

class PokemonType:
    def __init__(self, slot: int, type_: dict):
        self.slot = slot
        self.type = type_

class Pokemon(SimpleNamespace):
    @classmethod
    def from_json(cls, data: dict):
        # Convert abilities and types to objects, moves to a set of PokemonMove
        abilities = [PokemonAbility(**a) for a in data.get("abilities", [])]
        types = [PokemonType(slot=t["slot"], type_=t["type"]) for t in data.get("types", [])]
        moves = []
        moves_list = set()
        for move in data.get("moves", []):
            new_move = PokemonMove.from_json(move)
            move.append(new_move)
            moves_list.add(new_move.move.name)
        # Use SimpleNamespace for all other fields
        ns = cls(**data)
        ns.abilities = abilities
        ns.types = types
        ns.moves = moves
        return ns