#!/usr/bin/python3
import sys


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** i) / (b ** i)
        except Exception as e:
            print('Exception:', e, file=sys.stderr)
            return None
    result += b + a
    return result
