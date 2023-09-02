#!/usr/bin/python3
"""
A function that each and every element of a 2d list(matrix)
>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    A function that returns the element after divsion
    """
    # checking it is a matrix
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        #checking for the type of each element in the  matrix 
        if not isinstance(row,list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for column in row:
            # checking the type of each element in the list(row)
            if not isinstance(column, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    list_len = len(matrix[0])

    for row in matrix:
        # checking the length of the indiviual list element
        if len(row) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    #looping for and dividing each element of the list by 3
    # using list comprehension
    new_list =[[float(round(element/3,2)) for element in row ] for row in matrix]

    return new_list
