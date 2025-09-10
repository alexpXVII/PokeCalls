# PokeCalls

## Personal Note
This is a side project to refresh some of my skills while working on something fun. I intend to use it as a demonstration of my knowledge as a full-stack developer.

## Overview
PokeCalls is a Python application that simplifies interaction with the [PokeAPI](https://pokeapi.co/). It provides a structured way to fetch Pokémon data and includes a daily guessing game accessible via a command-line interface and a REST API.

## Features
-   **Python Library**: Easy-to-use services for fetching Pokémon and move data.
-   **REST API**: Django-based API to interact with the game logic.
-   **Daily Guessing Game**: Guess the daily secret Pokémon and move.
-   **Efficient**: Caching is used to minimize API calls.
-   **CLI**: A command-line interface for playing the game directly.
-   **Colorized Feedback**: The CLI provides colored hints for guesses.

## Upcoming Features

-   **Containerization with Docker**: Easily run and deploy the app in any environment using Docker containers.
-   **Frontend with React**: A modern web interface for interacting with the game.

## Installation

1.  Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd PokeCalls
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### Run the Django Server
To use the REST API, start the Django development server:

```bash
# Apply database migrations (good practice)
python manage.py migrate

# Start the server
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`.

### Run the CLI
To play the game in your terminal:
```bash
python src/main.py
```

## API Endpoints

### Guess the Pokémon
Send a `POST` request with your guess to this endpoint.

-   **URL**: `/api/guess-pokemon/`
-   **Method**: `POST`
-   **Body**: `{"guess": "pikachu"}`

**Example using cURL:**
```bash
curl -X POST http://127.0.0.1:8000/api/guess-pokemon/ \
-H "Content-Type: application/json" \
-d '{"guess": "pikachu"}'
```

### Guess the Move
Send a `POST` request with your guess to this endpoint.

-   **URL**: `/api/guess-move/`
-   **Method**: `POST`
-   **Body**: `{"guess": "mega-punch"}`

**Example using cURL:**
```bash
curl -X POST http://127.0.0.1:8000/api/guess-move/ \
-H "Content-Type: application/json" \
-d '{"guess": "mega-punch"}'
```

## Running Tests

To run the test suite using pytest:

```bash
pytest
```

## Project Structure

```
.
├── api/                # Django app for the API (views, urls)
├── pokecalls_project/  # Django project settings
├── src/                # Core Python library and CLI
│   ├── logic/          # Game logic and comparisons
│   ├── models/         # Data models
│   ├── services/       # Services for API calls
│   └── main.py         # CLI entry point
├── tests/              # Unit and integration tests
├── manage.py           # Django management script
└── requirements.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.