#!/usr/bin/python3
def multiple_returns(sentence: str) -> tuple:
    """This program returns the length of string and the first letter"""
    char = sentence[0]
    if sentence == "":
        return (0, None)
    return (len(sentence), char)
