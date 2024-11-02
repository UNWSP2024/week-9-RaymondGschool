# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random, io

def int_imput(text: str) -> int:
    while True:
        try:
            out: int = int(input(text))
            return out
        except ValueError:
            print("Please imput an integer.")

def put_random_into_file(count: int) -> None:
    # write to file, if it does not exist create it
    file: io.TextIOWrapper = open("numbers.txt", "w+")
    try:
        for x in range(count):
            file.write(f"{random.randrange(1,1000, 1)}")
            # prevent new line at end of the file
            if x < count - 1: file.write("\n")
    except:
        print("Error writing to file.")
    file.close()

if __name__ == "__main__":
    number_of_random: int = int_imput("How many random numbers do you want? ")
    put_random_into_file(number_of_random)