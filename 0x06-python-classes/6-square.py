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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (any): The length of one side of the square.
        """
        self._validate_size(size)
        self.__size = size
        self._validate_position(position)
        self.__position = position

    def _validate_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def _validate_position(self, position):
        if not isinstance(position, tuple) or len(position) != 2\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the new size of the square,
            validating for an integer and non-negative value.

        Args:
            new_size (int): The new size to be set.

        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        self._validate_size(value)
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self._validate_position(value)
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for y in range(self.size):
                for x in range(self.size):
                    if x + self.__position[0] >= 0:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print()
