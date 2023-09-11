#!/usr/bin/python3
""" Empty Class of Shapes"""


class BaseGeometry:
    """ A class for all shape"""
    def area(self):
        """
        Area is not yet implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A function that validate for int value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
