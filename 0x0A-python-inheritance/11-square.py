#!/usr/bin/python3
"""Module Square class """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    and represents a square shape.
    """

    def __init__(self, size):
        """
        Initialize the Square size.

        Args:
        - sze: The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Compute the area of the square.

        Returns:
        - The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        - A string in the format: [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
