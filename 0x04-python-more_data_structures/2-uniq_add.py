#!/usr/bin/python3
def uniq_add(my_list=[]) -> int :
    """This program returns the summation of unique numbers in a list"""
    #convert a list to a string for uniqueness
    my_set= set(my_list)
    #calculating the sum of the element in the list
    summation = sum(my_set)
    return summation
