#!/usr/bin/python3
def print_last_digit(number):
    abs_value = abs(number) % 10
    print("{}".format(abs_value), end="")
    return abs_value
