# config.py

# Base URL for the PokeAPI
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

# General Endpoints for PokeAPI (Resource Lists and Individual Resources)
# These are the top-level resources that allow you to list items
# or retrieve a specific item by name/ID.

# --- Core Endpoints ---
# Pokémon and related data
POKEMON_ENDPOINT = f"{POKEAPI_BASE_URL}pokemon/"
POKEMON_SPECIES_ENDPOINT = f"{POKEAPI_BASE_URL}pokemon-species/"
ABILITIES_ENDPOINT = f"{POKEAPI_BASE_URL}ability/"
MOVES_ENDPOINT = f"{POKEAPI_BASE_URL}move/"
TYPES_ENDPOINT = f"{POKEAPI_BASE_URL}type/"
STATS_ENDPOINT = f"{POKEAPI_BASE_URL}stat/"
NATURES_ENDPOINT = f"{POKEAPI_BASE_URL}nature/"
CHARACTERISTICS_ENDPOINT = f"{POKEAPI_BASE_URL}characteristic/"
EGG_GROUPS_ENDPOINT = f"{POKEAPI_BASE_URL}egg-group/"
GENDERS_ENDPOINT = f"{POKEAPI_BASE_URL}gender/"
GROWTH_RATES_ENDPOINT = f"{POKEAPI_BASE_URL}growth-rate/"
POKEATHLON_STATS_ENDPOINT = f"{POKEAPI_BASE_URL}pokeathlon-stat/"
LOCATIONS_ENDPOINT = f"{POKEAPI_BASE_URL}location/"
LOCATION_AREAS_ENDPOINT = f"{POKEAPI_BASE_URL}location-area/"
PAL_PARK_AREAS_ENDPOINT = f"{POKEAPI_BASE_URL}pal-park-area/"
REGIONS_ENDPOINT = f"{POKEAPI_BASE_URL}region/"

# Games and related data
GENERATIONS_ENDPOINT = f"{POKEAPI_BASE_URL}generation/"
POKEDEXES_ENDPOINT = f"{POKEAPI_BASE_URL}pokedex/"
VERSIONS_ENDPOINT = f"{POKEAPI_BASE_URL}version/"
VERSION_GROUPS_ENDPOINT = f"{POKEAPI_BASE_URL}version-group/"

# Items and related data
ITEMS_ENDPOINT = f"{POKEAPI_BASE_URL}item/"
ITEM_ATTRIBUTES_ENDPOINT = f"{POKEAPI_BASE_URL}item-attribute/"
ITEM_CATEGORIES_ENDPOINT = f"{POKEAPI_BASE_URL}item-category/"
ITEM_FLAVORS_ENDPOINT = f"{POKEAPI_BASE_URL}item-fling-effect/" # Corrected based on PokeAPI docs
ITEM_POCKETS_ENDPOINT = f"{POKEAPI_BASE_URL}item-pocket/"

# Evolution data
EVOLUTION_CHAINS_ENDPOINT = f"{POKEAPI_BASE_URL}evolution-chain/"
EVOLUTION_TRIGGERS_ENDPOINT = f"{POKEAPI_BASE_URL}evolution-trigger/"

# Machines
MACHINES_ENDPOINT = f"{POKEAPI_BASE_URL}machine/"

# Berries and related data
BERRIES_ENDPOINT = f"{POKEAPI_BASE_URL}berry/"
BERRY_FIRMNESSES_ENDPOINT = f"{POKEAPI_BASE_URL}berry-firmness/"
BERRY_FLAVORS_ENDPOINT = f"{POKEAPI_BASE_URL}berry-flavor/"

# Contests
CONTEST_TYPES_ENDPOINT = f"{POKEAPI_BASE_URL}contest-type/"
CONTEST_EFFECTS_ENDPOINT = f"{POKEAPI_BASE_URL}contest-effect/"
SUPER_CONTEST_EFFECTS_ENDPOINT = f"{POKEAPI_BASE_URL}super-contest-effect/"

# Encounters
ENCOUNTER_METHODS_ENDPOINT = f"{POKEAPI_BASE_URL}encounter-method/"
ENCOUNTER_CONDITIONS_ENDPOINT = f"{POKEAPI_BASE_URL}encounter-condition/"
ENCOUNTER_CONDITION_VALUES_ENDPOINT = f"{POKEAPI_BASE_URL}encounter-condition-value/"

# Utility (Languages)
LANGUAGES_ENDPOINT = f"{POKEAPI_BASE_URL}language/"

# Max Pokemon ID
MAX_POKEMON_ID = 1025
MAX_MOVE_ID = 921  # As of July 2025, PokeAPI has 921 moves

# --- Example Usage in a Wrapper (Illustrative) ---
# import requests
# from config import POKEMON_ENDPOINT
#
# def get_pokemon_data(pokemon_name_or_id):
#     # Note: For individual resources, you'd still append the name/ID
#     url = f"{POKEMON_ENDPOINT}{pokemon_name_or_id}/"
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()
#
# # To get a list of all Pokémon (paginated):
# # url = POKEMON_ENDPOINT # This URL already includes the base.
#
# # To get data for Pikachu:
# # pikachu_data = get_pokemon_data("pikachu")
# # print(pikachu_data)