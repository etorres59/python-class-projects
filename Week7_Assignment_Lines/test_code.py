# Evan Torres

from datetime import datetime

# This is a comment

# Prompt for Name
name = input("What's your name? ")

# Print Greeting
print(f"Hello, {name}")

age = int(input(f"{name}, how old are you? "))

current_year = datetime.now().year
birth_year = current_year - age

print(f"You were born around {birth_year}.")