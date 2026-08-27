###
# Name: Evan Torres
# Date: 6/19/26
# Program Name: Little Professor
# Program Purpose: Generate 10 addition problems at a chosen difficulty level
#                  and allow up to 3 attempts per problem.
###

import random


def main():
    # Get Difficulty
    level = get_level()
    # Initial Score
    score = 0

    # For loop to generate ten questions
    for i in range(10):
        # Randomly generate the numbers for the problem
        x = generate_integer(level)
        y = generate_integer(level)

        # Track the correct answer to check guesses against
        correct = x + y
        #Track Number of attempts
        attempts = 0

        # While attempts less than 3 keep prompting user to solve the problem
        while attempts < 3:
            # if correct add 1 to score
            try:
                user_answer = int(input(f"What is {x} + {y} = "))
                if user_answer == correct:
                    score += 1
                    break
                # If wrong print EEE and add 1 to attempts
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        # Show correct answer when attempts reaches 3
        if attempts == 3:
            print(f"The correct answer is: {correct}")
    #Print the Users total score
    print(f" Your Score: {score}/10")

# Function to that continually asks for difficulty level until it matches acceptable inputs
def get_level():
    while True:
        try:
            level = int(input("Please enter your Difficulty Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

# Helper Function that generates numbers depending on the difficulty level input
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()