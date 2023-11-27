#!/usr/bin/python3
"""empty class that defines rectangle"""


class Rectangle:
    """
    Represents a rectangle.

    Args:
        None
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Returns the current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Returns the current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle,
        handling special cases when width or height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """
        Returns a string representation
        of the rectangle using the character '#'.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for x in range(self.__height):
            for y in range(self.__width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        """
        Returns a repr representation of the rectangle.
        """
        return f"<3-rectangle.Rectangle object at {hex(id(self))}>"
