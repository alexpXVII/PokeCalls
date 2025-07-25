import config
from .utils import get_resource

def get_encounter_method(method_id_or_name, params=None):
    return get_resource(config.ENCOUNTER_METHODS_ENDPOINT, method_id_or_name, params)

def get_encounter_condition(condition_id_or_name, params=None):
    return get_resource(config.ENCOUNTER_CONDITIONS_ENDPOINT, condition_id_or_name, params)

def get_encounter_condition_value(value_id_or_name, params=None):
    return get_resource(config.ENCOUNTER_CONDITION_VALUES_ENDPOINT, value_id_or_name, params)