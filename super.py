"""
File:         super.py
Author:       Vu Nguyen
Date:         9/16/2020
Section:      31
Description:  Ask the user if they're either a hero or a villain. If
              villain ask for them name, if a hero ask how many ppl
              they saved.

"""


def super_power():
    hero_or_villain = input("Are you a Hero or a Villain? ").lower()
    if (hero_or_villain == "villain") or (hero_or_villain == "a villain"):
        vil_name = input("What is your villain's name? ")
        print(vil_name + " sounds pretty evil!")
    elif (hero_or_villain == "hero") or (hero_or_villain == "a hero"):
        ppl_saved = int(input("How many people have you saved? "))
        if ppl_saved <= 10:
            print("Go on more patrols!")
        elif ppl_saved < 100:
            print("Sounds like you're making a difference!")
        else:
            print("Wow, great job saving the city!")
    else:
        print("You need to enter either a hero or a villain")


super_power()
