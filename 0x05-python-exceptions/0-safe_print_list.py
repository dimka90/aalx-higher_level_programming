#!/usr/bin/python3
def safe_print_list(my_list=[], x=0) -> int:
    """a function that prints a specify  elements of a list
        and returns the number of element in the list
    """
    try:
        count = 0
        # creating a new list using list slicing
        new_list = my_list[:x]
        # using list comprehension to  print the element in the new list
        [print("{0:d}".format(num), end="") for num in new_list]
        # looping through the element if the list to cont them
        for num in new_list:
            count = count + 1
        print()
        # catching execeptions
    except (TypeError, ValuError, keyboardInterrupt):
        print("do not interupt")
    return count
