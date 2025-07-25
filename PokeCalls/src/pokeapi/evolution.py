import config
from .utils import get_resource

def get_evolution_chain(chain_id_or_name, params=None):
    return get_resource(config.EVOLUTION_CHAINS_ENDPOINT, chain_id_or_name, params)

def get_evolution_trigger(trigger_id_or_name, params=None):
    return get_resource(config.EVOLUTION_TRIGGERS_ENDPOINT, trigger_id_or_name, params)