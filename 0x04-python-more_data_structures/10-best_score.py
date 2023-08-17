#!/usr/bin/python3
def best_score(a_dictionary) -> int:
    """ a program that returns the max value if there is any"""
    # checking if a max num is found
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
