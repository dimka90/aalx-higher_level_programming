#!/usr/bin/python3
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
    except (ValueError,TypeError):
        pass
    return count
