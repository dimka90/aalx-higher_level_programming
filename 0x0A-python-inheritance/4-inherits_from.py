#!/usr/bin/python3
"""
checks if the object is a subclass  of a class
"""


def inherits_from(obj, a_class):
    """
    A function that checks if an object is from a particular
    or it is a subclass of a based class
    Args:
        obj(Object): Object Variable
        A_class: class vairable
    """
    obj_instance = issubclass(type(obj), a_class)

    if obj_instance:
        return True
    else:
        return False
