#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict) -> None:
    """Added a fuction that print a dictionary in sorted form"""
    if isinstance(a_dictionary, dict):
        sorted_keys = sorted(a_dictionary.keys())
        for key in sorted_keys:
            value = a_dictionary[key]
            print(f"{key}: {value}")
