#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate the area of a Reactangle
        Formular: width * height
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """
        calculate the perimeter of a rectangl
        formular: 2(Height + width)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2*(self.__width + self.__height)
        return perimeter

    def __str__(self):
        """
        The __str__ method defines the string representation of the object.

        Returns:
            str: A string representation of the object, including its name.

        Example:
            >>> obj = MyClass("example")
            >>> print(obj)
            "MyClass instance with name: example"
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for row in range(self.__height):
            rect_str += "#" * self.__width
            if row != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        The  method (__del__) is called when the object is being destroyed.
        This method is called when the object goes out of scope and is
        being garbage-collected.
        It prints a message indicating that the object is being destroyed.
        Note:
            The timing of when __del__ is called is not guaranteed and may vary
            depending on the Python implementation and the
            reference-counting mechanism.
        """
        print("Bye rectangle...")
