# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.
import io

def count_file_lines() -> None:
    ######################
    # Add your code here #
    ######################
    print('In the count_file_lines function')
    file: io.TextIOWrapper = open("names.txt", "r")

    #                   length of list, where each element is a line in the file
    number_of_names: int = len(file.readlines())
    print(F"Names in file: {number_of_names}")


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()