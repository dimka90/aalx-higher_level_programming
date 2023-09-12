#!/usr/bin/python3
"""
A module that save a python object to a file
"""
import json


def load_from_json_file(filename):
    """
    A function that saves a python object to a file
    Args:
        filename(str): file name
        Returns: The json object represtation of json file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
