from logic.game import Game

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def colorize_result(result: str) -> str:
    if "Match!" in result:
        return f"{GREEN}{result}{RESET}"
    elif "Wrong" in result:
        return f"{RED}{result}{RESET}"
    elif "N/A" in result:
        return result
    else:
        return f"{YELLOW}{result}{RESET}"

def main():
    player_name = input("Enter your name: ")
    game = Game(player_name)

    while True:
        print("\nMenu:")
        print("1. Guess the Pokémon")
        print("2. Guess the Move")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            pokemon = input("Guess the Pokémon (ID or name): ")
            results = game.guess_pokemon(pokemon)
            if results:
                for result in results:
                    print(colorize_result(result))
            print(f"Your guess: {pokemon}")

        elif choice == "2":
            move = input("Guess the Move (ID or name): ")
            results = game.guess_move(move, game.secret_move)
            if results:
                for result in results:
                    print(colorize_result(result))
            print(f"Your guess: {move}")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()