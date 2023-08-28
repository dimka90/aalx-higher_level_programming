#!/usr/bin/python3
def raise_exception() -> None:
    """
     a function that raises a type exception
     Return: None
    """
    try:
        result = 10 / 0
        raise ZeroDivisionError("Dvision by zero")
    except ZeroDivisionError as diverror:
        print("Divison:", diverror)
