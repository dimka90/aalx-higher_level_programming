#!/usr/bin/python
def multiple_returns(sentence: str) -> tuple:
    """This program returns the length of string and the first letter"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
