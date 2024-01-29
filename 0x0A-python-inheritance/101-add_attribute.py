#!/usr/bin/python3
"""
Module: add_attribute

This module provides a function to add a new
attribute to an object if it's possible.

Functions:
- add_new_attribute(obj, attr_name, attr_value):
Add a new attribute to an object if it's possible.
"""


def add_new_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.

    Args:
    - obj: The object to which the new attribute will be added.
    - attr_name: The name of the new attribute.
    - attr_value: The value of the new attribute.

    Raises:
    - TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
