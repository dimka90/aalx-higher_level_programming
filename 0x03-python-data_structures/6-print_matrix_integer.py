#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]) -> None:
    """This program print the a 2 X 2 matrix """
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" " if column != row[-1] else "")
        print()
