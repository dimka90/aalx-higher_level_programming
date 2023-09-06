#!/usr/bin/python3
"""
Text indention function
usage:
    text_indentation("Doing hard things. ")
"""


def text_indentation(text):
    """
     prints a text with 2 new lines after each of these char: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
