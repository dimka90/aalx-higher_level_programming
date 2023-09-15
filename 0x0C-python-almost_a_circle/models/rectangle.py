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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        set the width property of the rectangle
        """
        self.__width = width

    @property
    def height(self):
        """
        returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
         set the height property of the rectangle
        """
        self.__height = height

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
        self.__x = x

    @property
    def y(self):
        """
        returns the y of the rectangle
        """
        return self.__y

    @y.setter
    def height(self, y):
        """
         set the y property of the rectangle
        """
        self.__y = y
