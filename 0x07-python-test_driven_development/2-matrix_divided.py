#!/usr/bin/python3
"""
A function that each and every element of a 2d list(matrix)
>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix_divided( [[3, 9], [12, 15]], -3)
[[-1.0, -3.0], [-4.0, -5.0]]
"""


def matrix_divided(matrix, div):
    """
    A function that returns the element after divsion
    """
    # checking it is a matrix
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(message)
    for row in matrix:
        # checking for the type of each element in the  matrix
        if not isinstance(row, list):
            raise TypeError(message)
        for column in row:
            # checking the type of each element in the list(row)
            if not isinstance(column, (int, float)):
                raise TypeError(message)
    list_len = len(matrix[0])
    for row in matrix:
        # checking the length of the indiviual list element
        if len(row) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # looping for and dividing each element of the list by 3
    # using list comprehension
    # num = [float(round(element / 3, 2)) for element in row]
    if div < 0:
        new_list = [
            [float(round(element / -3, 2)) for element in row]
            for row in matrix
        ]
    else:
        new_list = [
            [float(round(element / 3, 2)) for element in row]
            for row in matrix
        ]
    return new_list
