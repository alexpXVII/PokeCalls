import config
from .utils import get_resource

def get_pokemon(pokemon_id_or_name, params=None):
    return get_resource(config.POKEMON_ENDPOINT, pokemon_id_or_name, params)

def get_pokemon_species(species_id_or_name, params=None):
    return get_resource(config.POKEMON_SPECIES_ENDPOINT, species_id_or_name, params)

def get_ability(ability_id_or_name, params=None):
    return get_resource(config.ABILITIES_ENDPOINT, ability_id_or_name, params)

def get_move(move_id_or_name, params=None):
    return get_resource(config.MOVES_ENDPOINT, move_id_or_name, params)

def get_type(type_id_or_name, params=None):
    return get_resource(config.TYPES_ENDPOINT, type_id_or_name, params)

def get_stat(stat_id_or_name, params=None):
    return get_resource(config.STATS_ENDPOINT, stat_id_or_name, params)

def get_nature(nature_id_or_name, params=None):
    return get_resource(config.NATURES_ENDPOINT, nature_id_or_name, params)

def get_characteristic(characteristic_id_or_name, params=None):
    return get_resource(config.CHARACTERISTICS_ENDPOINT, characteristic_id_or_name, params)

def get_egg_group(egg_group_id_or_name, params=None):
    return get_resource(config.EGG_GROUPS_ENDPOINT, egg_group_id_or_name, params)

def get_gender(gender_id_or_name, params=None):
    return get_resource(config.GENDERS_ENDPOINT, gender_id_or_name, params)

def get_growth_rate(growth_rate_id_or_name, params=None):
    return get_resource(config.GROWTH_RATES_ENDPOINT, growth_rate_id_or_name, params)

def get_pokeathlon_stat(stat_id_or_name, params=None):
    return get_resource(config.POKEATHLON_STATS_ENDPOINT, stat_id_or_name, params)