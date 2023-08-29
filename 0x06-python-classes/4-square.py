#!/usr/bin/python3


"""
Template of  square class
"""


class Square:
    """ Square class """
    def __init__(self, size=0) -> None:
        """ intialise a new square
         Args:
             size (int): a private attribute that keeps the size of the square
         Returns:
             None
         """
        self.__size = size

    def area(self) -> int:
        """Calculate the area of Square(Area = l * l)
        Args:
            self(object): instance of a square class
        Returns:
                Area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ retrieve the value of size
          Agrs:
              self(Object) : instance of the class square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ set the value of size
          Agrs:
              self(Object) : instance of the class square
              size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
