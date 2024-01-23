#!/usr/bin/python3
"""
This module defines the MyList class, a subclass of the built-in list class.
It includes a public instance method print_sorted,
which prints the list in ascending sorted order.

"""


class MyList(list):
    """
    A custom list class that inherits from the built-in
        `list` class and adds a method to print the list sorted.

    Attributes:
        None (inherits all attributes from the `list` class).

    Methods:
        print_sorted(): Prints the list elements in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        Args:
            None (uses the current list object).

        Returns:
            None (prints the sorted list to the console).
        """

        sorted_list = sorted(self)
        print(sorted_list)
