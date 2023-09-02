#!/usr/bin/python3
"""
A function that prints the name of an individual
>>> say_my_name("Dimka", "Yilrit")
My name is Dimka Yilrit
"""


def say_my_name(first_name, last_name=""):
    """
    Print the both firstname and surname
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if not first_name:
        raise ValueError("first_name can not be empty")
    print("My name is {} {}".format(first_name, last_name))
