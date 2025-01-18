"""Module for guessing a random number between 1 and 100."""

import random

while True:
    print("Generate a random number between 1 and 100:")
    randomNumber = random.randint(1, 100)

    while True:
        print("Guess a number between 1 and 100: (type 'q' to quit)")
        guess = input()
        if guess.lower() == "q":
            print("You ended the game...")
            exit()

        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Invalid input. Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        if guess < randomNumber:
            print("Your guess is too low.")
        elif guess > randomNumber:
            print("Your guess is too high.")
        else:
            print("You guessed the number!")
            break
