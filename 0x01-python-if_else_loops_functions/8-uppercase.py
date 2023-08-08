#!/usr/bin/python3
def uppercase(str):
    for counter in str:
        if (ord(counter) >= 97 and ord(counter) <= 122):
            counter = ord(counter) - 32
            print("{:c}".format(counter), end="")
        else:
            print("{}".format(counter), end="")
    print("")
