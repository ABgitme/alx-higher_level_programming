#!/usr/bin/python3
"""
This module defines the BaseGeometry class,
which serves as a foundation for geometric
operations and calculations.
"""


class BaseGeometry:
    """
    BaseGeometry class provides a foundation
    for geometric operations and calculations.
    """

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        - Exception: If the area() method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value to ensure it is an integer greater than 0.

        Args:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
