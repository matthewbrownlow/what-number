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
        except: ValueError:
            print("Invalid input. Please enter a valid number between 1 and 20.\n")


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 20.\n")

