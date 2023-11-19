#!/usr/bin/python3
from args import get_args
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arg = []
    operators = ['+', '-', '*', '/']
    arg = get_args()
    length = len(arg)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(get_args())
        exit(1)
    else:
        if arg[2] in operators:
            a = int(arg[1])
            b = int(arg[3])
            if arg[2] == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif arg[2] == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif arg[2] == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
