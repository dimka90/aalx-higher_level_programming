#!/usr/bin/python3
import sys


def safe_print_integer_err(value) -> bool:
    """
    A  function that prints an integer to stdout
    and also print error to the stderr.
    Return: boolean(true or false)
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
