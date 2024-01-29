#!/usr/bin/python3
"""
Module for working with rebellious integers.
This module provides the MyInt class, which inherits from int but
defiantly inverts the behavior of the == and != operators.
"""
class MyInt(int):
    """A rebellious integer class with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the behavior of the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behavior of the != operator."""
        return super().__eq__(other)
