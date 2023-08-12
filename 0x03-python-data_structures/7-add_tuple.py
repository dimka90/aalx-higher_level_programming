#!/urs/bin/python3
def add_tuple(tuple_a=(), tuple_b=()) -> tuple:
    """This program takes in two tuples and add them together"""
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) == 0:
            tuple_a = tuple_a + (0, 0)
        elif len(tuple_b) == 0:
            tuple_b = tuple_b + (0, 0)
        elif len(tuple_a) == 1:
            tuple_a = tuple_a + (0,)
        elif len(tuple_b) == 1:
            tuple_b = tuple_b + (0,)
        else:
            pass
    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    if len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    result = ()
    for counter in range(len(tuple_a)):
        element1 = tuple_a[counter]
        element2 = tuple_b[counter]
        add = element1 + element2
        result = result + (add,)
    return result
