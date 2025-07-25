import config
from .utils import get_resource

def get_location(location_id_or_name, params=None):
    return get_resource(config.LOCATIONS_ENDPOINT, location_id_or_name, params)

def get_location_area(location_area_id_or_name, params=None):
    return get_resource(config.LOCATION_AREAS_ENDPOINT, location_area_id_or_name, params)

def get_pal_park_area(area_id_or_name, params=None):
    return get_resource(config.PAL_PARK_AREAS_ENDPOINT, area_id_or_name, params)

def get_region(region_id_or_name, params=None):
    return get_resource(config.REGIONS_ENDPOINT, region_id_or_name, params)