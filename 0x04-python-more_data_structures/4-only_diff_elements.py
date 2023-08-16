#!/usr/bin/python3
def only_diff_elements(set_1: set, set_2: set) -> set:
    """A function that returns a set of all elements present in only one set"""
    new_list = set_1.symmetric_difference(set_2)
    return new_list
