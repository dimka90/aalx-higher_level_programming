#!/usr/bin/python3
def square_matrix_simple(matrix=[]) -> set:
    """ A function that squares and return a 2-d array"""
    result = []
    two_d = []
    for i in matrix:
        # using lambda and function function to a square a num
        result = list(map(lambda x: x ** 2, i))
        two_d.append(result)
    return two_d
