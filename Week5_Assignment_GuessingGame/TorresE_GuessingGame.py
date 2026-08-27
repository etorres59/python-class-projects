###
# Name: Evan Torres
# Date: 6/14/2026
# Program Name: Guessing Game
# Purpose: Generate a random number between 1 and a user-specified
#          level and repeatedly prompt the user to guess until correct.
###
import random

# Get a valid level(n) from the user
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Generate a random number between 1 and level(n)
secret_number = random.randint(1, level)

# Keep asking for guesses until the user is correct
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass