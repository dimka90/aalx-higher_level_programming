#!/usr/bin/python3
"""
A function that checks for a class instance
"""


def is_same_class(obj, a_class):
    """
    A function that checks for class instance
    Args:
       0bj(Obejct): instance of a class
       a_class: class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
