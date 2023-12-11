#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv


class Base:
    """
    Base class for all other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): The unique identifier
                of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the JSON string representation of a list of objects to a file.

        Args:
            list_objs (list): A list of objects that inherit from Base.
        """
        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as file:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string.

        Args:
            json_string (str): A JSON string
                representing a list of dictionaries.

        Returns:
            list: The list represented by the json_string.
        """
        if json_string is None:
            return []

        list_of_dicts = json.loads(json_string)
        return list_of_dicts

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class with all attributes set.

        Args:
            dictionary (dict): A dictionary
                containing the attributes and their values.

        Returns:
            Base: An instance of the class with all attributes set.
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances loaded from the file.
        """
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "r") as file:
                json_string = file.read()
                list_of_dicts = cls.from_json_string(json_string)
                return [cls.create(**obj) for obj in list_of_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """

        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads a list of instances from a CSV file.

        Returns:
            list: A list of instances loaded from the file.
        """
        list_of_objects = []
        file_name = f"{cls.__name__}.csv"
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 5:
                        if cls.__name__ == "Rectangle":
                            list_of_objects.append(cls(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4])))
                        elif cls.__name__ == "Square":
                            list_of_objects.append(cls(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])))
            return list_of_objects
        except FileNotFoundError:
            return []
