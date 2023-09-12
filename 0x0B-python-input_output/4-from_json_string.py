#!/usr/bin/python3
"""
A module that convert a json string to a python object
"""
import json


def from_json_string(my_str):
    """
    A function that return a json string to a python object
    Args:
         my_str(json string) : string to convert to python object
    """
    return json.loads(my_str)
