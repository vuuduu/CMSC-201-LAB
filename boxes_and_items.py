"""
File:         boxes_and_item.py
Author:       Vu Nguyen
Date:         11/10/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program implement two class, Box and Item,
              that user can create either item or box and place
              item into the box that they've create. 
"""
EMPTY = 0


class Box:
    def __init__(self, length, width, height):
        self.volume = height * width * length
        self.items = []
        self.unoccupied_space = self.volume

    def place(self, items):
        """
        Take the item object and place it into the list of item of that box.
        Check if the volume of the item is small enough to fit into the box.
        :param items: This is an item object
        :return: Nothing
        """
        if items.volume > self.unoccupied_space or self.unoccupied_space == EMPTY:
            print('The {} is too big!'.format(items.name))
        else:
            self.items.append(items)
            self.unoccupied_space -= items.volume

    def remove(self, items):
        """
        Take the item object and remove it from the item list.
        Check if the item is in the item list, for it to be remove.
        :param items: This is an item object
        :return: Nothing
        """
        if items not in self.items:
            print('The item {} is not in the box'.format(items.name))
        else:
            self.items.remove(items)
            self.unoccupied_space += items.volume


class Item:
    def __init__(self, names, length, height, width):
        self.name = names
        self.volume = length * height * width


if __name__ == '__main__':
    box_list = []
    item_list = []
    command = input('What do you want to do? ')
    while command.strip().lower() != 'quit':
        if command.strip().startswith('create box'):
            try:
                x, y, z = [int(x) for x in command.split()[2:]]
                box_list.append(Box(x, y, z))
            except:
                print('oops probably the wrong number of arguments')
        elif command.strip().startswith('create item'):
            name = command.split()[2]
            try:
                x, y, z = [int(x) for x in command.split()[3:]]
                item_list.append(Item(name, x, y, z))
            except:
                print('oops probably wrong number of arguments')

        elif command.strip().startswith('display boxes'):
            for i, box in enumerate(box_list):
                print("Box {}: with volume {} with {} space left".format(i + 1, box.volume, box.unoccupied_space))
                for item in box_list[i].items:
                    print('\t', item.name, 'is in the box.')

        elif command.strip().startswith('display items'):
            for i, item in enumerate(item_list):
                print("Item {}: with volume {}".format(item.name, item.volume))

        elif command.strip().startswith('place'):
            name_of_item = command.split()[1]
            the_item = None
            for item in item_list:
                if item.name == name_of_item:
                    the_item = item
            number_of_box = int(command.split()[3]) - 1
            if number_of_box in range(len(box_list)) and the_item:
                box_list[number_of_box].place(the_item)
            else:
                print('Error with box number or item name')

        elif command.strip().startswith('remove'):
            name_of_item = command.split()[1]
            the_item = None
            for item in item_list:
                if item.name == name_of_item:
                    the_item = item
            number_of_box = int(command.split()[3]) - 1
            if number_of_box in range(len(box_list)) and the_item:
                box_list[number_of_box].remove(the_item)
            else:
                print('Error with box number or item name')
        command = input('What do you want to do? ')
