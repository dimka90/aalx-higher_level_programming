#!/usr/bin/python3
def uppercase(str):
    str_len = len(str)
    upper = ""
    for counter in str:
        if (ord(counter) >= 97 and ord(counter) <= 122):
            counter = ord(counter) - 32
            upper = upper + "{:c}".format(counter)
        else:
            upper = upper + "{}".format(counter)
    print(upper)
