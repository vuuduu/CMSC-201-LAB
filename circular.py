"""
File:         circular.py
Author:       Vu Nguyen
Date:         10/6/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs determine how many times the
              string is a rotation of itself.
"""

if __name__ == "__main__":

    # Part 2B - Removing Whitespace
    user_input = (input("Enter a string: ").strip()).lower()
    user_input = user_input.split()
    user_input = "".join(user_input)

    """ Part 2C - Transversing and edited string
    counter = 0
    for char in user_input:
        print(counter, char, end=' ')
        counter += 1
    print()
    """

    # Part 2C - Circular Rotation Check
    offset = 0
    is_Rotation = False
    monitor_string = 'x'

    for k in range(1, len(user_input)):
        compare_string = ''

        # Math expression that rotates string
        compare_string += user_input[k:] + user_input[0:k]
        offset += 1

        # Check if there are no rotation in the string
        if (len(monitor_string) + 1) == len(user_input):
            print("There are no rotations for this string")
        else:
            # If there are a match value then display the offset
            if compare_string == user_input:
                is_Rotation = True
                while is_Rotation:
                    print(user_input, "is a rotation with offset", offset)
                    is_Rotation = False
            else:
                monitor_string += "x"

