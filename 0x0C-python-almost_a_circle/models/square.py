#!/usr/bin/python3
"""
A python module that inherit from the Parent Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates square objects with 2 dimensions and offset coordinates.
    Uses super-superclass `Base` __init__ to create valid instance id
    and passes args to superclass `__init__` to set attributes. Does not
    create its own attributes. `size` acts as alias for `width`/`height`.

    Args:
        size (int): x and y dimensions of square
        x (int): horizontal offset of square
        y (int): vertical offset of square
        id (int): unique identifer for each instance of super().super()

    Project task:
        10. And now, the Square! - class Square `__init__`, `__str__`,
            only inherited validation, no new attributes

    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        A function that overide it parent string representation
        """
        return "{} ({:d}) {:d}/{:d} - {}".format(
                "Square", self.id, self.x, self.y, self.width)
