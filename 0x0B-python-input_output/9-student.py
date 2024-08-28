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
    to_json():
        Returns a dictionary representation of the Student instance.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
        --------
        dict:
            A dictionary containing the student's
            first name, last name, and age.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
