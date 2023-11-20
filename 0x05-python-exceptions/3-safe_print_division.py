#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return None
    finally:
        if ZeroDivisionError:
            c = None
        print("Inside result: {}".format(c))
