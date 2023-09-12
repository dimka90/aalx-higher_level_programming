#!/usr/bin/python3
""" A module that represent a Student class"""


class Student:
    """
    """
    def __init__(self, first_name, last_name, age):
        """
        initiate class vairables
        Args:
            self(object): Instance of the student class
            firt_name(str): firstname of the student
            last_name(str): lastname of the student
            age(int)       : Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return the dictionary representation of the Student Class"""
        attr = type(attrs)
        if (attr == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
