#!/usr/bin/python3
"""
Module: peak_finder

This module contains a function to find
a peak in a list of unsorted integers.

Function:
- find_peak(list_of_integers): Finds a peak in the list_of_integers.

Note:
- There may be more than one peak in the list.
- The algorithm used in the function has a time
complexity of O(log n), where n is the number of elements in the list.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - peak: A peak element from the list.
    """
    # Get the length of the list
    n = len(list_of_integers)

    # Handle edge cases
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]

    # Binary search to find a peak
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid - 1] and\
                list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
