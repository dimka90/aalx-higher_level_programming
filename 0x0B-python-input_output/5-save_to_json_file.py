#!/usr/bin/python3
"""
A module that save a python object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that saves a python object to a file
    Args:
        my_obj(Oject): python object to to be written to the file
        filename(str): file name
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
