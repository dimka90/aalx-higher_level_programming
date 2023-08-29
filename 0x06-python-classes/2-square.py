#!/usr/bin/python3


"""
Template of  square class
"""


class Square:
    """ Square class """
    def __init__(self, size=0) -> None:
        """
         Args:
             size (int): a private attribute that keeps the size of the square
         Returns:
             None
         """
        if not isinstance(size, int):
            raise TypeError("size must ne an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
