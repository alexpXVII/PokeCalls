import config
from .utils import get_resource

def get_berry(berry_id_or_name, params=None):
    return get_resource(config.BERRIES_ENDPOINT, berry_id_or_name, params)

def get_berry_firmness(firmness_id_or_name, params=None):
    return get_resource(config.BERRY_FIRMNESSES_ENDPOINT, firmness_id_or_name, params)

def get_berry_flavor(flavor_id_or_name, params=None):
    return get_resource(config.BERRY_FLAVORS_ENDPOINT, flavor_id_or_name, params)