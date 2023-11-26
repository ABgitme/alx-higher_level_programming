#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name {} {}".format(first_name,last_name))