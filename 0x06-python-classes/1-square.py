#!/usr/bin/python3
"""
This class represents a square.
"""


class Square:
    """
    Represents a square shape with four equal sides and four right angles.

    Attributes:
        _size (float): The length of one side of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
            size (any): The length of one side of the square.
        """
        self.__size = size
