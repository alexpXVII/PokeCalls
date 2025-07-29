from types import SimpleNamespace
from typing import List, Optional, Dict, Any

class PokemonMove(SimpleNamespace):
    @classmethod
    def from_json(cls, data: dict):
        # Assign all fields from the JSON to the namespace
        ns = cls(**data)
        return ns