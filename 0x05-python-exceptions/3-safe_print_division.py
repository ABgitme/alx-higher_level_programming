#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError or NameError:
        return None
    finally:
        if ZeroDivisionError or NameError:
            c = None
        print("Inside result: {}".format(c))
