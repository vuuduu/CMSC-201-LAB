"""
File:         favorite_nums.py
Author:       Vu Nguyen
Date:         10/20/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs request for user to input a person name
              and their favorite number. It then check to see if that
              number is already in someone else's list, and display
              whether the number is in other person list or added to
              their own list. Lastly, it'll print out the list the
              person favorite numbers.
"""


def print_favorite_numbers(who, favorites_dict):
    print(favorites_dict[who])


def add_favorite_number(who, number, favorites_dict):

    num_in_list = False

    # Check to see if the name is already exist in the dictionary
    if who not in favorites_dict:
        favorites_dict[who] = []

    # Cycle through each name and see if the number is already in someone else's fav_list
    for Name in favorites_dict:
        if number in favorites_dict[Name]:
            print(number, "was found in " + Name + "'s favorite list")
            num_in_list = True

    # check to see if the favorite number is unique from everyone else and added to that person
    if not num_in_list:
        favorites_dict[who].append(number)
        print(number, "added to " + who + "'s favorites")


if __name__ == '__main__':
    favorites = {}
    in_string = input('What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ')
    while in_string.strip().lower() != 'quit':
        if in_string.strip().lower().startswith('print favorite numbers for'):
            print_favorite_numbers(in_string.strip().split()[-1], favorites)
        if len(in_string.split()) == 2:
            name, num = in_string.split()
            num = int(num)
            add_favorite_number(name, num, favorites)

        in_string = input('What do you want to do (add favorite number), or quit? ')
