#!/usr/bin/python3
def safe_print_integer(value) -> bool:
    """a function that prints an integer with "{:d}".format()
    Retunn: true on success and false on failure
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        return False
