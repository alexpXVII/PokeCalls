from models.pokemon import Pokemon
from models.move import Move
from typing import List, Any

def compare_numbers(val1: int, val2: int) -> str:
    if val1 == val2:
        return "Match!"
    if val1 is None or val2 is None:
        return "N/A"
    return "Higher" if val1 > val2 else "Lower"

def compare_values(val1: Any, val2: Any) -> str:
    if val1 == val2:
        return "Match!"
    return "Wrong"
    
def compare_pokemon(pokemon1: Pokemon, pokemon2: Pokemon) -> List[str]:
    results = []
    results.append(f"Name: {compare_values(pokemon1.name, pokemon2.name)}")
    results.append(f"Height: {compare_values(pokemon1.height, pokemon2.height)}")
    results.append(f"Weight: {compare_values(pokemon1.weight, pokemon2.weight)}")
    return results

def compare_moves(move1: Move, move2: Move) -> List[str]:
    results = []

    # Helper to extract attribute safely
    def get_attr(obj, attr, subattr=None):
        value = getattr(obj, attr, None)
        if subattr and isinstance(value, dict):
            return value.get(subattr)
        return value

    # Type
    type1 = get_attr(move1, "type", "name")
    type2 = get_attr(move2, "type", "name")
    results.append(f"Type: {compare_values(type1, type2)}")

    # Category (damage_class)
    cat1 = get_attr(move1, "damage_class", "name")
    cat2 = get_attr(move2, "damage_class", "name")
    results.append(f"Category: {compare_values(cat1, cat2)}")

    # Power
    results.append(f"Power: {compare_numbers(get_attr(move1, 'power'), get_attr(move2, 'power'))}")

    # PP
    results.append(f"PP: {compare_numbers(get_attr(move1, 'pp'), get_attr(move2, 'pp'))}")

    # Accuracy
    results.append(f"Accuracy: {compare_numbers(get_attr(move1, 'accuracy'), get_attr(move2, 'accuracy'))}")

    # Target
    target1 = get_attr(move1, "target", "name")
    target2 = get_attr(move2, "target", "name")
    results.append(f"Target: {compare_values(target1, target2)}")

    # Has Effect
    effect1 = bool(get_attr(move1, "effect_entries"))
    effect2 = bool(get_attr(move2, "effect_entries"))
    results.append(f"Has Effect: {compare_values(effect1, effect2)}")

    return results