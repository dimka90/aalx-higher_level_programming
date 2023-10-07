#!/usr/bin/pytho3
"""A module that have contain a base class for shapes"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """
        A function that takes in a  dictionary and modify the attribute
        of the temp_object the values from the dictionary
        class to update the values of the temporal object
        args:
            **dictionary(dict): a dictionary with key and values
        """
        # Checking to see if the name of the object belongs to the rectangle
        # class
        if cls.__name__ == 'Rectangle':
            # Creating a temporal variable with arbitary values
            temp_obj = cls(1, 2, 3)
        if cls.__name__ == 'Square':
            temp_obj = cls(5, 5)
            # calling the update function on the temp_obj to update it values
        temp_obj.update(**dictionary)
        return temp_obj

    @classmethod
    def load_from_file(cls):
        """
        A function that loads object instance from a file and convert
        it to python object
        """
        import os.path

        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding="utf-8") as file:
                json_data = file.read()
        else:
            return []
        obj_list = cls.from_json_string(json_data)
        instance_list = []
        for item in obj_list:
            instance_list.append(cls.create(**item))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to file a CSV formatted string of a list of dictionary
        representations of objects of `Base` derived classes.

        Args:
            list_objs (list) of (dict): list of `Base` derived objects (in
                this project `Rectangle` and `Square`)

        Project tasks:
            20. JSON ok, but CSV? - class method `save_from_file_csv()`
                returns list of instances from file <Class name>.csv, or empty
                list if no file. must use `from_json_string()` and `create()`,
                class of instances in list depends on cls

        """
        if list_objs is None:
            list_objs = []

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns list of instances from file <class name>.csv, or empty list
        if no file. `cls` determines class of instances.

        Returns:
            list of instances of `cls` from file <class name>.csv, or empty
                list if no file

        Project tasks:
            20. JSON ok, but CSV? - class method `load_from_file_csv()`
                returns list of instances from file <Class name>.csv, or empty
                list if no file. must use `from_json_string()` and `create()`,
                class of instances in list depends on cls

        """
        import os.path

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        filename = cls.__name__ + '.csv'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                instance_list = []
                for row in csv_reader:
                    for key in keys:
                        row[key] = int(row[key])
                    instance_list.append(cls.create(**row))
                return instance_list
        else:
            return []
