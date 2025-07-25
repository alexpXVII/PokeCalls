import config
from .utils import get_resource

def get_machine(machine_id_or_name, params=None):
    return get_resource(config.MACHINES_ENDPOINT, machine_id_or_name, params)