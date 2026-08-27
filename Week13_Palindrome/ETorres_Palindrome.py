###
# Name: Evan Torres
# Date: 8/2/26
# Program Name: Palindrome
# Program Purpose: Implement a program with a recursive function, is_pal,
# that returns True if the string argument is a palindrome and False if it is not.
###

def is_pal(word):

    # Base Case
    if len(word) <= 1:
        return True

    # Recursive Case
    if word[0] != word[-1]:
        return False

    return is_pal(word[1:-1])

# Answer Helper Function
def answer(word):
    if is_pal(word) == True:
        return "Yes"
    else:
        return "No"

# to_chars Helper Function
def to_chars(word):
    new_word = ""

    for char in word:
        if char.isalpha():
            new_word += char.lower()

    return new_word

def main():
    user_input = input("Please enter a string: ")

    clean_word = to_chars(user_input)

    print(f"Is {user_input} a palindrome? {answer(clean_word)}")


if __name__ == '__main__':
    main()