#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """a function that prints a specify  elements of a list"""
    try:
        count = 0
        new_list = my_list[:x]
        [print(num, end="") for num in new_list]
        print()
        for count in new_list:
            count = count + 1
    except (TypeError, ValuError, keyboardInterrupt):
        print("do not interupt")
    return count - 1
