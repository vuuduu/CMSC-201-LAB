"""
File:    hailstone.py
Started: by Dr. Gibson
Author:  Vu Nguyen
Date:    11/3/2020
Section: 31
E-mail:  vnguye12@umbc.edu
Description: This file contains python code that implements the
             "flight" of a hailstone, following the HOTPO rules
             (also known as the Collatz Conjecture), recursively

NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
PART OF A FORMULA/MATHEMATICAL CONJECTURE

############################################################
flight() recursively calculates the path of a hailstone
Input:   the height of the hailstone
Output:  a recursive call, which at the end returns
         the number of "steps" taken for the
         hailstone to reach a height of 1
"""


def flight(height):

    # BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0
    # stops when it reaches height of 1 (the ground)
    if height <= 0:
        print('Invalid height of {}'.format(height))
        return 0
    elif height == 1:
        print('Height of {}'.format(height))
        return 0

    # RECURSIVE CASES:
    # if the current height is even, divide it by 2 (Even height)
    # if the current height is odd, multiply it by 3, then add 1 (odd height)
    if height % 2 == 0:
        print('Height of {}'.format(int(height)))
        return flight(height / 2) + 1

    else:
        print('Height of {}'.format(int(height)))
        return flight(height * 3 + 1) + 1


def main():

    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    start_height = int(input(msg))

    # recursive call goes here
    steps = flight(start_height)

    print("\nIt took", steps, "steps to hit the ground.")

    print("Thank you for using the Hailstone Simulator!\n")


main()
