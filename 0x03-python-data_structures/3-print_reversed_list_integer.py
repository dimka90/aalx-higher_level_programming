#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]) -> None:
    """This function print a list in reverse order"""
    list_len = len(my_list) - 1
    for counter in range(list_len, -1, -1):
        print("{}".format(my_list[counter]))
