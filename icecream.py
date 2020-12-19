"""
File:         icecream.py
Author:       Vu Nguyen
Date:         9/20/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program contain two list Ice cream flavor
              and ice cream topping. Display each ice cream
              flavor with each topping except for strawberry.

"""

if __name__ == "__main__":
    ice_cream_flavors = ["vanilla", "strawberry", "chocolate"]
    toppings = ["caramel", "marshmallow", "gummi bears"]

    for flavors in ice_cream_flavors:
        for top in toppings:
            print(flavors, "is tasty with", top)
        if "strawberry" in ice_cream_flavors:
            print("strawberry is fine on its own!")
            ice_cream_flavors.remove("strawberry")
