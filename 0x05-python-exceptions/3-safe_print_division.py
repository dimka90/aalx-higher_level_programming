#!/usr/bin/python3
def safe_print_division(a: int, b: int) -> int or None:
    """
    A function that divides 2 integers and prints the result
    Return : result of division or None if division is by zero
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        # checking for the value of result
        if result is not None:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
    return result
