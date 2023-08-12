#!/usr/bin/python
def multiple_returns(sentence: str) -> tuple:
    """This program returns the length of string and the first letter"""
    char = sentence[0]
    if len(sentence) == 0:
        char = None
    return (len(sentence), char)
