#!/usr/bin/python3
def safe_print_list(my_list=[], x=0) -> int:
    """a function that prints a specify  elements of a list"""
    try:
        count = 0
        new_list = my_list[:x]
        [print("{0:d}".format(num), end="") for num in new_list]
        for num in new_list:
            count = count + 1
        print()
    except (TypeError, ValuError, keyboardInterrupt):
        print("do not interupt")
    return count
