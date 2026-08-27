###
# Name: Evan Torres
# Date: 7/19/26
# Program Name: CookieJar
# Program Purpose: Implements a Cookie Jar class that stores cookies while enforcing
# capacity and size constraints using properties and setters.
###

import sys

# Represents a cookie jar with a limited storage capacity.
class Jar:

    def __init__(self, capacity=12):
        # Initialize the current number of cookies.
        self._size = 0

        # Use the property setter so validation is applied.
        self.capacity = capacity

    # Return a visual representation of the cookies in the jar
    def __str__(self):
        return "🍪" * self.size

    # Add cookies
    def deposit(self, n):
        self.size = self.size + n

    # Remove cookies
    def withdraw(self, n):
        self.size = self.size - n

    @property
    # Return the maximum number of cookies the jar can hold
    def capacity(self):
        return self._capacity

    # Set the jar's capacity after validating the new value.
    @capacity.setter
    def capacity(self, capacity):

        # Capacity must: Be an integer, Be zero or greater,
        # Not be smaller than the current number of cookies
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an integer")

        if capacity < 0:
            raise ValueError("Capacity cannot be less than zero")

        if capacity < self.size:
            raise ValueError("Capacity cannot be less than size")

        self._capacity = capacity

    @property
    #Return the current number of cookies in the jar
    def size(self):
        return self._size

    # Update the number of cookies in the jar.
    @size.setter
    def size(self, size=0):

        # Size must: Be zero or greater, Not exceed the jar's capacity
        if size < 0:
            raise ValueError("Size cannot be less than zero")

        if size > self.capacity:
            raise ValueError("No more space in the jar")

        self._size = size

#Validate command-line arguments and demonstrate the Jar class
def main():

    # Ensure exactly one command-line argument is provided.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Convert the command-line argument to an integer.
    try:
        capacity = int(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not an integer")

    # Create a cookie jar with the requested capacity.
    jar = Jar(capacity)

    # Demonstrate depositing cookies.
    jar.deposit(10)
    print(jar)
    print(jar.size)
    print(jar.capacity)

    # Demonstrate withdrawing cookies.
    jar.withdraw(2)
    print(jar)
    print(jar.size)
    print(jar.capacity)

    # Demonstrate updating the size using the property setter.
    jar.size = 12
    print(jar)
    print(jar.size)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()