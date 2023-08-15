#!/usr/bin/python3
def multiple_returns(sentence: str) -> tuple:
    """This program returns the length of string and the first letter"""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
