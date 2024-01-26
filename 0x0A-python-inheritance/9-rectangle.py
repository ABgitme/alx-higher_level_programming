#!/usr/bin/python3
"""Module Rectangle class """
BaseGeometry = __import__("8-rectangle").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    and represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        Args:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
        - The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        - A string in the format: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
