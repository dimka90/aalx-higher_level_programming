#!/usr/bin/python3
"""
This module read content from a file
"""


def read_file(filename=""):
    """
    This function opens a file for reading and print the
    content
    Args:
        filename(obj): name of the file to open for reading

    """
    # using the with context manager to open a file for reading
    with open(filename, "r", encoding="utf-8") as file:
        f = file.read()
        print(f, end="")
