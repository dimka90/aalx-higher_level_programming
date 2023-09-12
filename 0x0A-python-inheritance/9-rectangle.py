#!/usr/bin/python3
"""A module that for Rectangular shape."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class"""

    def __init__(self, width, height):
        """
           A function that performs a check before initialisation
           Args:
               width(int): width of the rectangle
               height(int): height of the rectangle
           Returns:
                  None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate the area of a Rectanle
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        string representation of an object
        """
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
