#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""
    str_len = len(str)
    if n < 0 or n > str_len:
        return str

    for counter in range(0, str_len):
        if counter == n:
            continue
        else:
            new_str += str[counter]
    return new_str
