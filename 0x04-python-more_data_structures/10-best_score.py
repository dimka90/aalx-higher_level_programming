#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = max(a_dictionary, key=lambda key: a_dictionary[key] if a_dictionary[key] is not None else float('-inf'))
    max_value = a_dictionary[max_key]
    return max_value
