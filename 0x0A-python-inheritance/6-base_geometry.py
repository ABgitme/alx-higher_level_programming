#!/usr/bin/python3
"""
This module defines the BaseGeometry class,
which serves as a foundation for geometric
operations and calculations.
"""


class BaseGeometry:
    """
    BaseGeometry class provides a foundation for geometric operations and calculations.
    """

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        - Exception: If the area() method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")
