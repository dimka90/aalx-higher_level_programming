#!/usr/bin/python3
"""
This module defines a function to find a peak in a list of unsorted integers.

Module Usage:
    from module_name import find_peak

Function:
    find_peak(list_of_integers)

    Finds a peak in a list of unsorted integers.

    Parameters:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: The peak element in the list. If the list is
                     empty or None,returns None. If the list has
                     only one element,returns that element.
    Notes:
        - The algorithm has the lowest possible complexity.
        - There may be more than one peak in the list.

Example:
    >>> find_peak([1, 2, 4, 6, 3])
    6
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Parameters:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: The peak element in the list. If the list is
                     empty or None,returns None. If the list has
                     only one element, returns that element.

    Notes:
        - The algorithm has the lowest possible complexity.
        - There may be more than one peak in the list.

    Example:
        >>> find_peak([1, 2, 4, 6, 3])
        6
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_idx = int(len(list_of_integers) / 2)

    if mid_idx != len(list_of_integers) - 1:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] and\
           list_of_integers[mid_idx + 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
    else:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
        else:
            return list_of_integers[mid_idx - 1]

    if list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
        a_list = list_of_integers[0:mid_idx]
    else:
        a_list = list_of_integers[mid_idx + 1:]

    return find_peak(a_list)
