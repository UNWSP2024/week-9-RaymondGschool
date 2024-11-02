# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
import io, os
def sum_numbers_from_file() -> None:
    ######################
    # Add your code here #
    ######################
    # if file does not exist
    if not os.path.isfile("numbers.txt"):
        print("File: 'numbers.txt' does not exist")
        return
    file: io.TextIOWrapper = open("numbers.txt", "r")

    final_sum: int = 0
    for number in file.readlines():
        try:
            out: int = int(number)
            final_sum += out
        except ValueError:
            print(f"Error converting: '{number}' to int. Defaulting to 0")

    print(f"Sum of all numbers in file: {final_sum}")
    
# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()