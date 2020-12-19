"""
File:         crab.py
Author:       Vu Nguyen
Date:         9/29/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs ask for a list of crab weights. Then
              the user will specify which weights should be remove.
"""

if __name__ == "__main__":

    crab_weight = []
    crab_weight_input = input("Enter crab weight, (STOP to end) ")

    while crab_weight_input != "STOP":
        crab_weight.append(float(crab_weight_input))
        crab_weight_input = input("Enter crab weight, (STOP to end) ")

    light_or_heavy = input("Do you want to keep light or heavy crabs? ")

    while (light_or_heavy != "light") and (light_or_heavy != "heavy"):
        print("You must enter light or heavy!")
        light_or_heavy = input("Do you want to keep light or heavy crabs? ")

    determining_weight = float(input("What weight determines whether a crab is light or heavy? "))

    remove = []
    keep = []

    if light_or_heavy == 'light':
        for weight in crab_weight:
            if weight < determining_weight:
                keep.append(weight)
            else:
                remove.append(weight)
        print("You're keeping the crabs with weight", keep)
        print("You're not keeping the crabs with weight", remove)
    else:
        for weight in crab_weight:
            if weight > determining_weight:
                keep.append(weight)
            else:
                remove.append(weight)
        print("You're keeping the crab with weight", keep)
        print("You're not keeping the crab with weight", remove)
