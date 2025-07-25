import config
from .utils import get_resource

def get_language(language_id_or_name, params=None):
    return get_resource(config.LANGUAGES_ENDPOINT, language_id_or_name, params)