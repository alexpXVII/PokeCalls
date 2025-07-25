from logic.game import Game

def main():
    player_name = input("Enter your name: ")
    game = Game(player_name)
    pokemon = input("Guess the Pokémon (ID or name): ")
    results = game.guess_pokemon(pokemon)
    for result in results:
        print(result)

    print(f"Your guess: {pokemon}")

if __name__ == "__main__":
    main()