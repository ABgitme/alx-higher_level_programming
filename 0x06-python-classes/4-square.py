#!/usr/bin/python3
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
    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (any): The length of one side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
    @property
    def size(self):
        return self.__size