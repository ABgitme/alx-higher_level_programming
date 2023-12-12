#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The x coordinate of the square. Defaults to 0.
            y (int, optional): The y coordinate of the square. Defaults to 0.
            id (int, optional):
                The unique identifier of the object. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square."""
        if args:  # If args is not empty, skip kwargs
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        else:  # Update attributes based on kwargs
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """String representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }
