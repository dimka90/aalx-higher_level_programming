#!/usr/bin/python3
for counter in range(97, 123):
    if chr(counter) == 'q' or chr(counter) == 'e':
        continue
    print("{}".format(chr(counter)), end="")
