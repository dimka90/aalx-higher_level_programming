#!/usr/bin/python3
"""
A python module that convert an objec to a dictionary
"""


def class_to_json(obj):
    """
    A function that returns the dictionary represantation
    of an object
    """
    return obj.__dict__
