#!/usr/bin/python3
import sys


def main():
    sum = 0
    for counter in sys.argv[1:]:
        sum = sum + int(counter)
    print(sum)


if __name__ == "__main__":
    main()
