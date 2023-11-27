#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the `max_integer` function.

    The `max_integer` function takes a list of integers as input
    and returns the maximum integer in the list.
    If the list is empty, the function returns None.

    Args:
        None
    """
    def test_max_integer(self):
        """
        Test that the `max_integer` function
        returns the maximum integer in a list.

        Args:
            None
        """
        maxval = max_integer(([1, 10, 3, 4]))
        self.assertEqual(maxval, 10)
        maxval = max_integer([])
        self.assertIsNone(maxval)
        maxval = max_integer([2, 2, 2])
        self.assertEqual(maxval, 2)
