import config
from .utils import get_resource

def get_generation(generation_id_or_name, params=None):
    return get_resource(config.GENERATIONS_ENDPOINT, generation_id_or_name, params)

def get_pokedex(pokedex_id_or_name, params=None):
    return get_resource(config.POKEDEXES_ENDPOINT, pokedex_id_or_name, params)

def get_version(version_id_or_name, params=None):
    return get_resource(config.VERSIONS_ENDPOINT, version_id_or_name, params)

def get_version_group(version_group_id_or_name, params=None):
    return get_resource(config.VERSION_GROUPS_ENDPOINT, version_group_id_or_name, params)