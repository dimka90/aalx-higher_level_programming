#!/usr/bin/python3
"""
This function print  a sqaure of hash(#)
symbol
"""


def print_square(size):
    """
    print the # according to the number passed
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if (size < 0) and isinstance(size, float) or size < 0:
        raise TypeError("size must be >= 0")
    # if size == 0:
    #   print()
    # printing each element in 2d
    for i in range(0, size):
        for x in range(0, size):
            print("#", end="")
        print()
