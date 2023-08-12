#!/usr/bin/python3

def max_integer(my_list=[]) -> int:
    """Return the maximun number in a list"""
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]
        for counter in my_list:
            if counter > max:
                max = counter
    return max
