#!/usr/bin/python3

"""
Template of  square class
"""


class Square:
    """ Square class """
    def __init__(self, size: int) -> None:
        """
        Args:
            size (int): a private attribute that keeps the size of the square
        Returns:
            None
        """
        self.__size = size
