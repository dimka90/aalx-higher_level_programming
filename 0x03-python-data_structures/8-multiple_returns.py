#!/usr/bin/python3
def multiple_returns(sentence: str) -> tuple:
    char = sentence[0]
    """This program returns the length of string and the first letter"""
    if sentence == "":
        return (0, None)
    return (len(sentence), char)
