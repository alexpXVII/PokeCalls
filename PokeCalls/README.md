# PokeCalls

## Overview
PokeCalls is a Python library that simplifies interaction with the [PokeAPI](https://pokeapi.co/). It provides a structured way to fetch Pokémon data, moves, and related resources, and includes helper classes and services for building games or tools using Pokémon data.

## Features
- Easy-to-use API client for REST calls
- Models for Pokémon, moves, and related data
- Service layer with caching for efficient API usage
- Example game logic for daily Pokémon guessing
- Modular and extensible codebase

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Fetch a Pokémon

```python
from services.pokemon_service import PokemonService

pokemon = PokemonService.fetch_pokemon("squirtle")
print(pokemon.name, pokemon.height, pokemon.weight)
```

### Fetch a Move

```python
from services.move_service import MoveService

move = MoveService.fetch_move("mega-punch")
print(move.name, move.power, move.accuracy)
```

### Example: Daily Pokémon Game

```python
from logic.game import Game

game = Game("Ash")
result = game.guess_pokemon("pikachu")
print(result)
```

## Running Tests

To run unit tests:

```bash
pytest
```

## Project Structure

```
src/
├── models/      # Data models for Pokémon, moves, etc.
├── services/    # Service layer for API calls and caching
├── logic/       # Game logic and application code
├── pokeapi/     # API endpoint wrappers and utilities
├── config.py    # Configuration and constants
└── main.py      # Example entry point
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.