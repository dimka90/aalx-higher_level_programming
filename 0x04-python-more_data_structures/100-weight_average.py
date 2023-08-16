#!/usr/bin/python3
def weight_average(my_list=[]) -> float:
    """A function that returns the weighted average of all integers tuple"""
    """ formular for weight_average """
    # W_Average = (Value1 * Weight1 + Value2 * Weight2) / (Weight1 + Weight)
    if not my_list:
        return 0
    sum = 0
    total = 0
    average = 0
    for counter in my_list:
        element = counter[0]
        element2 = counter[1]
        result = element * element2
        sum = sum + result
        total = total + element2
    average = sum/total
    return average
