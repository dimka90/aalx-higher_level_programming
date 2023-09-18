#!/usr/bin/pytho3
"""A module that have contain a base class for shapes"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A functiopn that converts a lists of python python dictionary
        to it json equavalent
        """
        if list_dictionaries is None:
            return "{}".format("[]")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A function that that saves the state of an object to a json file
        args:
             cls(class method): cls means a class method
             list_s(list): list of dictionary obeject to be save to the file
        """
        if list_objs is None:
            list_objs = []
        list_dict = []
        # looping through all the objec in the list
        for obj in list_objs:
            # Extracting each object attribute to key and value pair
            # making a new dictionary
            obj_to_dict = obj.to_dictionary()
            # Add the object instance dictionary to the list
            list_dict.append(obj_to_dict)
        # convert the dictionary to json string
        json_string = cls.to_json_string(list_dict)
        # adding the class name and .json extension to every fiel
        filename = cls.__name__ + '.json'
        # Saving the state of the object of a file using the
        # with context manager
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        A function that convert a json_string dictionary
        into a python object
        """
        if json_string is None or json_string == ' ':
            return []

        return json.loads(json_string)
