###
# Name: Evan Torres
# Date:6/28/26
# Program Name: Lines
# Program Purpose: Counts the number of lines of code in a Python file,
# excluding blank lines and comments.
###

import sys


def main():
    # Check number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check file extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                stripped = line.lstrip()

                # Skip blank lines
                if stripped == "":
                    continue

                if stripped.strip() == "":
                    continue

                # Skip comments
                if stripped.startswith("#"):
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()