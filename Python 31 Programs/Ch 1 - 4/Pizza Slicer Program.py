## Pizza Slicer Program
## Program to help understand the concept of slicing
## Demonstrates string slicing

word = "pizza"

print (
"""
    Slicing 'Cheat Sheet'

    0   1   2   3   4   5
    +---+---+---+---+---+
    | p | i | z | z | a |
    +---+---+---+---+---+
    -5 -4  -3  -2  -1

    """
)

print ("Enter the beginning and ending index for your slice of 'pizza'.")
print ("Press the Enter key at 'Start' to exit.")
start = None
while start != "":
    start = (input("\nStart:\t"))

    if start:
        start = int(start)

        finish = int(input("Finish:\t"))

        print ("word[", start, ":", finish, "] is", end = " ")
        print (word[start:finish])

input ("\n\nPress the Enter key to exit")
