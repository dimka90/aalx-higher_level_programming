#!/usr/bin/python3
"""
A module that returns a string representation of an object
"""
import json


def to_json_string(my_obj):
    """
    A function that convert a python object to string json
    Agrs:
       my_object(object) : object to convert
    """
    return json.dumps(my_obj)
