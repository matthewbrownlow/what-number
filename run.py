import random

logo = """
 /$$      /$$ /$$                   /$$           /$$   /$$                         /$$                           /$$$$ 
| $$  /$ | $$| $$                  | $$          | $$$ | $$                        | $$                          /$$  $$
| $$ /$$$| $$| $$$$$$$   /$$$$$$  /$$$$$$        | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$|__/\ $$
| $$/$$ $$ $$| $$__  $$ |____  $$|_  $$_/        | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$   /$$/
| $$$$_  $$$$| $$  \ $$  /$$$$$$$  | $$          | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/  /$$/ 
| $$$/ \  $$$| $$  | $$ /$$__  $$  | $$ /$$      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$       |__/  
| $$/   \  $$| $$  | $$|  $$$$$$$  |  $$$$/      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$        /$$  
|__/     \__/|__/  |__/ \_______/   \___/        |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/       |__/
"""


def generate_secret_number():
    """
    Generate a number between 1 and 20.
    """
    return random.randint(1, 20)


def get_player_guess():
    """
    Gets the player's guess as an integer.
    """
    while True:
        try:
            guess = int(input("Take a guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 20.\n")


def check_guess(secret_number, guess):
    """
    Check the player's guess against the secret number and provide feedback
    based on provided integer.
    """
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} correctly!")
        return True
    elif guess < secret_number:
        print("Too low! Try a higher number.\n")
    else:
        print("Too high! Try a lower number.\n")
    return False


def play_game():
    """
    Main game loop for the number guessing game.
    """
    while True:
        print(logo)
        print("Welcome to the Number Guessing Game!\n")
        print("I'm thinking of a number between 1 and 20.\n")
        secret_number = generate_secret_number()

        attempts = 0
        max_attempts = 5

        while attempts < max_attempts:
            guess = get_player_guess()
            attempts += 1

            if check_guess(secret_number, guess):
                break
        else:
            print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    play_game()