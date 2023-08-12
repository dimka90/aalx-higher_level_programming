#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]) -> None:
    """This program print the a 2 X 2 matrix """
    for counter in matrix:
        for i in counter:
            print(" {:d}".format(i), end="")
        print("")
