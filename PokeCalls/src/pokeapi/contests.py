import config
from .utils import get_resource

def get_contest_type(contest_type_id_or_name, params=None):
    return get_resource(config.CONTEST_TYPES_ENDPOINT, contest_type_id_or_name, params)

def get_contest_effect(contest_effect_id_or_name, params=None):
    return get_resource(config.CONTEST_EFFECTS_ENDPOINT, contest_effect_id_or_name, params)

def get_super_contest_effect(super_contest_effect_id_or_name, params=None):
    return get_resource(config.SUPER_CONTEST_EFFECTS_ENDPOINT, super_contest_effect_id_or_name, params)