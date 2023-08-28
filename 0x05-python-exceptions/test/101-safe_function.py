#!/usr/bin/python3
import sys


def safe_function(fct, *args) -> float, int or None:
    """
    a function that executes a function safely.
    This program takes in a function and try to
    execute the function
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
  
  
