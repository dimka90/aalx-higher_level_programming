#!/usr/bin/python3
def print_last_digit(number):
    abs_value = abs(number) % 10
    if number < 0:
        return - abs_value
    else:
        return abs_value
