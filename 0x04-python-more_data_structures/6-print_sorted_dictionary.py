#!/usr/bin/python3
def print_sorted_dictionary(dictionary) -> None:
    def custom_sort_key(item):
        value = item[1]
        return (type(value).__name__, value)
    sorted_items = sorted(dictionary.items(), key=custom_sort_key)

    for key, value in sorted_items:
        print("{}: {}".format(key, value))
