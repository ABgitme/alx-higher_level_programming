#!/usr/bin/python3

"""
This module defines a Student class to
represent a student with basic attributes.
"""


class Student:
    """
    A class used to represent a Student.

    Attributes:
    -----------
    first_name : str
        The first name of the student.
    last_name : str
        The last name of the student.
    age : int
        The age of the student.

    Methods:
    --------
    to_json(attrs=None):
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings,
        only the specified attributes are retrieved.
        Otherwise, all attributes are retrieved.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Parameters:
        -----------
        first_name : str
            The first name of the student.
        last_name : str
            The last name of the student.
        age : int
            The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Parameters:
        -----------
        attrs : list, optional
            A list of strings representing the attribute names to retrieve.

        Returns:
        --------
        dict:
            A dictionary containing the requested
            attributes of the student.
            If attrs is None or not a list of strings,
            all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
