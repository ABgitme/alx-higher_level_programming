#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
        lastdig = number % 10
        return lastdig
    else:
        lastdig = number % 10
        return lastdig
