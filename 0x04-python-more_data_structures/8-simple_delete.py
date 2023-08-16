#!/usr/bin/python3
def simple_delete(a_dictionary: dict, key="") -> None:
    """ Deleted an element from a dictionary"""
    if key in a_dictionary:
        del dictionary[key]
