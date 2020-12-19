"""
File:         major.py
Author:       Vu Nguyen
Date:         9/16/2020
Section:      31
Description:

"""


def major():
    academic_major = input("What is your major? ").upper()
    if (academic_major == "CMSC") or (academic_major == "CMPE"):
        print("You need to earn at least a B for CMSC 201 to count.")
    else:
        print("You need to earn at least a C for CMSC 201 to count.")


major()
