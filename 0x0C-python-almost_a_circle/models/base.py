#!/usr/bin/pytho3
"""A module that have contain a base class for shapes"""


class Base:
    """
    A class that Create a bass class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        A function that instantiate vairable
        Args:
            self(object): instance of a class
            id(int): id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
