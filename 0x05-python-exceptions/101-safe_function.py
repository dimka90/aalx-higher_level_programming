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
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    except ZeroDivisionError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    except IndexError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
