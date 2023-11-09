#!/usr/bin/python3
def square(x):
    return x**2

def square_matrix_simple(matrix=[]):
    squared_matrix = list(map(lambda row: list(map(square, row)), matrix))
    return squared_matrix