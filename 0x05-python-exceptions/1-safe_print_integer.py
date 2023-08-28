#!/usr/bin/python3
def safe_print_integer(value) -> bool:
    """a function that prints an integer with "{:d}".format()
    Retunn: true on success and false on failure
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
