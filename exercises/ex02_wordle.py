""" Wordle recreation"""

__author__ = "730648844"


def contains_char(word: str, char: str) -> bool:
    """Search for the letter in the word"""

    # Makes sure the char varaible length is 1
    assert len(char) == 1, f"len('{char}') is not 1"

    # counter variable
    i = 0

    # Runs through the word and will return true if the letter is anywhere in the word
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a display similar to wordle, with colors matching if letters match"""

    # Makes sure that the guess and secret word are equal
    assert len(guess) == len(secret), "Guess must be same length as secret"

    # Colors for the wordle like display
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # Counter varaible
    i = 0

    # Where the colors will be stored
    output: str = ""

    # Will search through the guess and assigns a color based on whether a letter is in
    # the word and if its in the right location
    while i < len(guess):
        if secret[i] == guess[i]:
            output += GREEN_BOX
            i += 1
        elif contains_char(secret, guess[i]) is True:
            output += YELLOW_BOX
            i += 1
        else:
            output += WHITE_BOX
            i += 1

    return output


def input_guess(expected_length: int) -> str:
    """Where the user inputs their guess, and it is checked that it is the correct
    length"""
    # User inputs their guess
    guess: str = str(input(f"Enter a {expected_length} character word:"))

    # Will keep asking the user to input a word with the correct length until they do
    while len(guess) != expected_length:
        guess = str(input(f"That wasn't {expected_length} chars! Try again:"))

    return str(guess)


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    # Counter/keeps track of how many round the user has used
    rounds = 1

    # Maximum number of rounds the user has to guess correctly
    max_rounds = 6

    # While the user has rounds, the program will keep prompting for guesses. When all
    # rounds are used up, user will have lost, but if the user input the correct word
    # they get a congratulation message.
    while rounds <= max_rounds:

        # Pring what round the user is on
        print(f"===Turn {rounds}/6===")

        # Keeps tract of what the current guess is to compare later
        current_guess = input_guess(len(secret))

        # Cuases the printout of the colors
        print(emojified(current_guess, secret))

        # If the word is right, game is over, if word is not right, will increase the
        # counter variable by 1
        if current_guess == secret:
            print(f"You won in {rounds}/6 turns!")
            return None
        else:
            rounds += 1

    # If by the end of all rounds the user has not guessed correctly, will print a
    # loosing message.
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
