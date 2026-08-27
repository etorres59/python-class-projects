###
# Name: Evan Torres
# Date:4/7/26
# Program Name: twttr
# Program Purpose: Prompts the user for a string of text
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.
###

import re

def main():
    #Prompt user for input
    user_message = input("Please enter your message: ")

    # Remove vowels (pattern, replacement, string, flag case-insensitive )
    new_message = re.sub(r"[aeiou]", "", user_message, flags=re.IGNORECASE)

    #print new string
    print("Output:", new_message)


if __name__ == "__main__":
    main()