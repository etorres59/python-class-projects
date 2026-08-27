###
# Name: Evan Torres
# Date: 7/12/26
# Program Name: Scourgify
# Program Purpose: splits names into first and last names, and writes
# the data to a new CSV file.
###

import sys
import csv

def main():
   # Check for correct number of command-line arguments
   if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
   elif len(sys.argv) <3:
        sys.exit("Too few command-line arguments")

   # Set Arguments to variables
   input_file = sys.argv[1]
   output_file = sys.argv[2]

   # Check if File is CSV
   if not input_file.endswith(".csv"):
      sys.exit("Invalid Type. Choose a CSV file")

   try:
      # Open input file for reading
      with open(input_file, "r", newline="") as infile:
         reader = csv.DictReader(infile)

         # Open outputfile for writing
         with open(output_file, "w", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])

            # Use first line to create Header (first,last, house)
            writer.writeheader()

            # Split each name from the input file into first and last
            for row in reader:
               last, first = row["name"].split(",")

               # Write each row with first, last, and house into output file
               writer.writerow({"first": first, "last": last, "house": row["house"]})

   except FileNotFoundError:
      sys.exit(f"Could not read {input_file}")

if __name__ == '__main__':
   main()
