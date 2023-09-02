#!/usr/bin/python3
"""
This program add the integer
>>> add_integer(5,6)
11
"""


def add_integer(a, b=98):
    """
    This function add and returns the sum of two numbers
    """
    # checking for type int or float
    if not isinstance(a, (int, float, complex)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float, complex)):
        raise TypeError("b must be an integer")
    # casting both the value of a and b to integer
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
