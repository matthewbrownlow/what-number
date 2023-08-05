# What Number?
> [Click here to view the live website on GitHub Pages](https://what-number-c26ae6113643.herokuapp.com/) Please note: To open any links in this document in a new browser tab, please press `Cmd ⌘ + Click` (Mac) or `CTRL + Click` (Windows/Linux)

- The Number Guessing Game is a simple Python text-based game where the player tries to guess a secret number randomly generated between 1 and 20. The game starts by welcoming the player and informing them of the number range. The player has a maximum of 5 attempts to guess the secret number correctly. After each guess, the game provides feedback, indicating whether the guess is too high or too low.

- If the player correctly guesses the secret number within the allowed attempts, the game congratulates them and asks if they want to play again. If the player exhausts all attempts without guessing the correct number, the game informs them of the secret number and asks if they want to play again.

- The player can choose to continue playing the game or exit by entering `yes` or `no` when prompted to play again. The game loop repeats as long as the player wants to continue playing.

- The game offers a fun and interactive experience for players, challenging their guessing skills while providing opportunities for improvement in subsequent attempts.

![Screenshot of am i responsive website displaying the Heroku hosted What Number? app on four different devices](assets/images/README.md/what-number-am-i-responsive.png)

## How to play
To play the number guessing game, follow these steps:

- Run the Python script that contains the game code. You can execute the script using a Python interpreter on your computer.

- The game will start with a cool ASCII art logo displaying the title `What Number?`.

- The game will welcome you to the Number Guessing Game and inform you that it has `picked a random number between 1 and 20`.

- You need to guess the secret number chosen by the game.

- Enter your guess as an integer when prompted. Make sure your guess is a number between 1 and 20.

- The game will inform you if your guess is correct or not. If it's correct, the game will congratulate you, and the round will end.

- If your guess is incorrect, the game will provide feedback, telling you if the secret number is `higher` or `lower` than your guess.

- You have a `total of 5 attempts` to guess the correct number. If you don't guess correctly within these attempts, the round ends.

- After each round, the game will ask you if you want to play again. To play another round, enter `yes` when prompted. If you don't want to play again, enter anything other than `yes`, and the game will end.

- The game will keep running as long as you choose to play again. You can keep playing and trying to guess the secret number in each round.

- Remember, the game is all about trying to guess the secret number within a limited number of attempts. Use the feedback provided by the game to make better guesses in each round.

- Have fun playing the Number Guessing Game and see if you can guess the secret number correctly!

## Features
### Existing Features
#### Terminal Game Start
- Here the terminal displays the `Running statup command: python3 run.py`
- Game `ASCII logo` introducing you to the game `Welcome to the Number Guessing Game!`
- Propting you to enter a value between 1 and 20 `I'm thinking of a number between 1 and 20.` following the `Take a guess: ` value input.

![Screenshot of beginning game terminal](assets/images/README.md/terminal-game-start.png)

#### Correct Answer Guessed
- Here the terminal displays a value fo `5` entered into the `Take a guess: ` value input, with a following message of `Congratulations! You guessed the number 5 correctly!` as the secret number was the value of `5`.
- Displaying another value input to restart the game `Do you want to play again? (yes/no): `.

![Screenshot of correct answer guessed](assets/images/README.md/terminal-game-correct-guess.png)

#### Answer Guessed too Low
- Here the terminal displays a value fo `2` entered into the `Take a guess: ` value input, with a following message of `Too low! Try a higher number.` as the secret number is higher than the value entered.
- Prompting the user to enter another value `Take a guess: `.

![Screenshot of incorrect answer guessed, answer too low](assets/images/README.md/terminal-game-incorrect-guess-too-low.png)

#### Answer Guessed too High
- Here the terminal displays a value fo `17` entered into the `Take a guess: ` value input, with a following message of `Too high! Try a lower number.` as the secret number is lower than the value entered.
- Prompting the user to enter another value `Take a guess: `.

![Screenshot of inccorect answer guessed, answer too high](assets/images/README.md/terminal-game-incorrect-guess-too-high.png)

#### Incorrect Value Entered
- Here the terminal displays an error message `Invalid input. Please enter a valid number between 1 and 20.` stating that the value entered is not a valid input.
- Prompting the user to enter another value between `1` and `20`.

![Screenshot of incorrect value entered, error message](assets/images/README.md/terminal-game-incorrect-value-entered-error-message.png)

