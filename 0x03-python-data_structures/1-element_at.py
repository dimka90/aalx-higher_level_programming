#!/usr/bin/python3
def element_at(my_list: list, idx: int) -> int:
    if idx < 0 or idx >= len(my_list):
        return None
    """returns the an element at a particular index"""
    return my_list[idx]
