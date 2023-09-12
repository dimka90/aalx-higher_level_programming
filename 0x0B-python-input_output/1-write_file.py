#!/usr/bin/python3
"""
A module that write to a file
"""


def write_file(filename="", text="") -> int:
    """
    A function that write to a file and return the name
    number of the character written to the file
    Args:
        filename(obj): name of file to write
        text(str): text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        count = file.write(text)
        return count
