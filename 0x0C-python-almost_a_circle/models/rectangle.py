#!/usr/bin/python3
"""A module that contains a rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    A Rectangle classs
    Arg:
       Base(Class): Parent class of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiation of vairable
        args:
            self(object): object of the Class Rectangle
            width:(int): width of the rectangle
            height(int): height of the rectangle
            x(int)
            y(int):
            id(int) or None for Default
        Return:
               None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width property of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
         set the height property of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        returns the width of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
         set the x property of the rectangle
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x:
            if x < 0:
                raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        returns the y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
         set the y property of the rectangle
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y:
            if y < 0:
                raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        A function that calcluate the area of a rectangle
        formular
               Area = height(length) * width
        args:
            self(object): Instance of a Rectangle Class
        Return:
              Area of the Rectangle
        """
        area = self.height * self.width

        return area

    def display(self):
        """
        A function that display a grid of rectangle with the # pound
        """
        for row in range(self.height):
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of the function
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                "Rectangle", self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """
        A function that update the values of the instance vairable of a class
        args:
            *args(no positional argument): receive any length of variable
        """
        if len(args) == 0:
            raise ValueError("An empty call to update function")

        for index, item in enumerate(args):
            if index == 0:
                if self.id != item:
                    self. id = item
            elif index == 1:
                self.width = item
            elif index == 2:
                self.height = item
            elif index == 3:
                self. x = item
            elif index == 4:
                self.y = item
