#!/usr/bin/python3
"""
A python module that create a base class for all shapes
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
         a function that
        """
        if id is not None:
            self.id = id
            Base.__nb_objects += 1
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def get_ob_count(cls):
        """
        a function that
        """
        return cls.__nb_objects
