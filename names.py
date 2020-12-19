"""
File:         names.py
Author:       Vu Nguyen
Date:         10/13/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs ask for user inputted list of string or
              use an already existence list of string to calculate
              the sum of each element in the list.
"""


def sum_list(numbers):
    sum_of_integers = 0

    for value in numbers:
        sum_of_integers += value

    return sum_of_integers


# This function gets the length of each name in the list and add into the list_of_integer
def get_string_lengths(string):
    list_of_integers = []

    for name in string:
        list_of_integers.append(len(name))

    return list_of_integers


# This function is to get name from user and added into a list
def get_names():
    list_of_names = []
    a_name = input("Enter a name, STOP to stop: ").strip()

    while a_name != "STOP":
        list_of_names.append(a_name)
        a_name = input("Enter a name, STOP to stop: ").strip()

    return list_of_names


if __name__ == "__main__":
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]

    kitties_sum = sum_list(get_string_lengths(kitties))
    print("There are", kitties_sum, "letters in kitties.")

    puppies = [
        "Charlie",
        "Chuck",
        "Chuckadero"
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]

    puppies_sum = sum_list(get_string_lengths(puppies))
    print("There are", puppies_sum, "letters in puppies.")

    your_sum = sum_list(get_string_lengths(get_names()))
    print("There are", your_sum, "letters in the names you entered.")
