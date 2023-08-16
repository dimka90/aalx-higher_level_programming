#!/usr/bin/python3
def multiply_by_2(a_dictionary: dict) -> dict:
    """ A function that multiply the values of dictionary by 2"""
    new_dict = {}
    for key in a_dictionary:
        """asigining values to the new list """
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
