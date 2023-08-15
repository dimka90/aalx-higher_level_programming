#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()) -> tuple:
    """This program takes in two tuples and add them together"""
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]
    # Take only the first two elements of each tuple and add them
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
