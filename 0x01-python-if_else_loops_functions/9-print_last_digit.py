#!/usr/bin/python3
def print_last_digit(number):
    abs_value = abs(number) % 10
    if number < 0:
        print("{0:d}".format(- abs_value))
        return - abs_value
    else:
        print("{0:d}".format(abs_value))
        return abs_value
