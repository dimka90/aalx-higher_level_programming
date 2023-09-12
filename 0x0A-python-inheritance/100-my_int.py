#!/usr/bin/python3
"""
A Module that modify some of the methods of the based class(int)
"""


class MyInt(int):
    """custom int class"""

    def __eq__(self, value):
        """
        negating equal to sig (==) to not equal too (!=)
        Note: This function overide the default behvaiour
        """
        not_equal_to = self.real != value
        return not_equal_to

    def __ne__(self, value):
        """
        Negate the not equals (!=) to (==)
        Note: it overide the default behaviour
        """

        equal_to = self.real == value
        return equal_to
