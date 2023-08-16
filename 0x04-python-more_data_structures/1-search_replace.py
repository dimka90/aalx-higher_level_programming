#!/usr/bin/python3
def search_replace(my_list: list, search: int, replace: int) -> list:
    """A function that replaces an item in list with a new one"""
    new_list = []
    for i in my_list:
        # checking for a match
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
