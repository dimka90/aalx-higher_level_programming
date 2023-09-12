#!/usr/bin/python3
"""
A module that Represent a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class
    """

    def __init__(self, size):
        """
        Initialise an instance of a class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
