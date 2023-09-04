#!/usr/bin/python3
"""
This is a class Rectangle
"""


class Rectangle:
    """ Class Rectangle"""
    def __init__(self, width=0, height=0) -> None:
        """
        Args:
             width(int): a private attribute that stores the width
             height(int): a private atribute that stores the height
        Returns:
              None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            This function returns the width of the rectangle
            Args:
                 self(obeject): instance of the new class
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
              This function returns the width of the rectangle
              Args:
                   self(obeject): instance of the new class
                   value(int) : width of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
            This function returns the width of the rectangle
            Args:
                 self(obeject): instance of the new class
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
              This function returns the width of the rectangle
              Args:
                   self(obeject): instance of the new class
                   value(int) : height of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
