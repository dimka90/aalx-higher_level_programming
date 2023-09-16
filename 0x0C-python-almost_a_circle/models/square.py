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

    @property
    def size(self) -> int:
        """
        Returns the value of size
        size is an alias for both height and width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Validate the value of size before assignment
        size is an alias for width, so it is same thing as
        validating the width of thesquare
        """
        self.width = value

    def update(self, *args, **kwargs):
        """
        A function that update the values of an instancewq
        of the Square class
        """

        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 4:
                raise TypeError("Len of dictionary is between 1 and 4")

            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise TypeError("Invalid key provided")
        elif len(args) > 4:
            raise TypeError("len of positonal argument is 1 to 4")
        else:
            for index, item in enumerate(args):
                if index == 0:
                    self.id = item
                elif index == 1:
                    self.size = item
                elif index == 2:
                    self.x = item
                elif index == 3:
                    self.y = item

    def to_dictionary(self) -> dict:
        """
        A dictionary representation of the Square class

        return:
              a dictionary representation of the attribute of an object
        """

        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['size'] = self.size
        self_dict['x'] = self.x
        self_dict['y'] = self.y

        return self_dict
