###
# Name: Evan Torres
# Date: 6/6/26
# Program Name: Vending Machine Coin Counter
# Purpose: Simulate a vending machine that accepts only 25, 10, and 5 cent coins
#          and keeps asking the user for coins until at least 50 cents is inserted.
###
# The price of everything in the vending machine
PRICE = 50

# This will track how much money the user has inserted so far
total_inserted = 0

# These are the ONLY valid coins the machine accepts
valid_coins = [25, 10, 5]

# Keep looping until the user has paid at least 50 cents
while total_inserted < PRICE:

    # Ask the user to insert a coin
    coin = int(input("Insert Coin: "))

    # Only accept valid coins (ignore anything else)
    if coin in valid_coins:
        total_inserted += coin

        # Check how much is still owed after a valid coin is added
        if total_inserted < PRICE:
            print("Amount due:", PRICE - total_inserted)
    else:
        # Ignore invalid coins completely (no change to total)
        print("Invalid Coin Entered. Try Again.")

# Once loop ends, user has paid 50 or more
change = total_inserted - PRICE

# Output change owed (if 0 then "No change needed"
if change > 0:
    print("Change owed:", change)
else:
    print("No change needed.")