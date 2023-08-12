#!/usr/bin/python3
def new_in_list(my_list: list, idx: int, element: int) -> list:
    """create a new list and modify it the new list"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    # slice[:] create a new copy of the list in memory
    # the contain of the new list is copied to the new list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
