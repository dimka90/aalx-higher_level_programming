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
    """
    with open(filename, "r", encoding="utf-8") as file:
        json.load( file)
