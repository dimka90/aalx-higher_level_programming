#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0) -> set:
    """Returns the multipy a new list by multiple of 2"""
    return (list(map(lambda n: n * number, my_list)))
