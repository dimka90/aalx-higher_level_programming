#!/usr/bin/python3
def fizzbuzz():
    for counter in range(1, 101):
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz", end=" ")
        elif counter % 3 == 0:
            print("Fizz", end=" ")
        elif counter % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(counter), end=" ")
