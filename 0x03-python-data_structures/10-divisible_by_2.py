#!/usr/bin/python3
def divisible_by_2(my_list=[]) -> list:
    """This program returns a list based on divisibility of a number by 2"""
    new_list = []
    for counter in my_list:
        if counter % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
