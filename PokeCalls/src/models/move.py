from types import SimpleNamespace
from typing import List, Optional, Dict, Any

# Example response from https://pokeapi.co/api/v2/move/5/
# {
#   "id": 5,
#   "name": "mega-punch",
#   "accuracy": 85,
#   "effect_chance": null,
#   "pp": 20,
#   "priority": 0,
#   "power": 80,
#   "type": {"name": "normal", "url": "..."},
#   "damage_class": {"name": "physical", "url": "..."},
#   "generation": {"name": "generation-i", "url": "..."},
#   "effect_entries": [...],
#   "meta": {...},
#   "names": [...],
#   "learned_by_pokemon": [...],
#   "flavor_text_entries": [...],
#   "stat_changes": [...],
#   "target": {"name": "selected-pokemon", "url": "..."},
#   "contest_type": {...},
#   "contest_effect": {...},
#   "super_contest_effect": {...},
#   ...
# }

class Move(SimpleNamespace):
    @classmethod
    def from_json(cls, data: dict):
        # Assign all fields from the JSON to the namespace
        ns = cls(**data)
        return ns