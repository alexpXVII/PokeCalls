import config
from .utils import get_resource

def get_item(item_id_or_name, params=None):
    return get_resource(config.ITEMS_ENDPOINT, item_id_or_name, params)

def get_item_attribute(attribute_id_or_name, params=None):
    return get_resource(config.ITEM_ATTRIBUTES_ENDPOINT, attribute_id_or_name, params)

def get_item_category(category_id_or_name, params=None):
    return get_resource(config.ITEM_CATEGORIES_ENDPOINT, category_id_or_name, params)

def get_item_flavor(flavor_id_or_name, params=None):
    return get_resource(config.ITEM_FLAVORS_ENDPOINT, flavor_id_or_name, params)

def get_item_pocket(pocket_id_or_name, params=None):
    return get_resource(config.ITEM_POCKETS_ENDPOINT, pocket_id_or_name, params)