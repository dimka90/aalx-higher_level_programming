def exclusive_elements(set1, set2):
    exclusive_set = set()

    for element in set1:
        if element not in set2:
            exclusive_set.add(element)

    for element in set2:
        if element not in set1:
            exclusive_set.add(element)

    return exclusive_set

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
result = exclusive_elements(set1, set2)
print(result)  # Output: {1, 2, 6, 7}
