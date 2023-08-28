#!/usr/bin/pythin3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        index = my_list[x - 1]
        new_list = my_list[:x]
        for num in new_list:
            if isinstance(num, int):
                print("{:d}".format(num), end="")
                count = count + 1
        print()
    except IndexError:
        print("Out of list index")
    except ValueError:
        print("Not an int")
    return count
