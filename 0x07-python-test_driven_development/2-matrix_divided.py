#!/usr/bin/python3
"""function that divides all elements of a matrix and return new matrix"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a scalar value.

    Args:
        matrix (List[List[int | float]]): The matrix to be divided.
        div (int | float): The scalar value to divide by.

    Raises:
        TypeError: If the matrix is not a list of lists,
            if the matrix contains elements that are not integers or floats,
                or if `div` is not an integer or float.
        ZeroDivisionError: If `div` is zero.

    Returns:
        List[List[float]]: A new matrix with each element divided by `div`.
    """
    new_matrix = []
    row_lengths = []
    if matrix is None:
        raise TypeError("matrix must be a matrix(list of lists) "
                        "of integers/floats")
    for row in matrix:
        row_lengths.append(len(row))
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for element in row:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix(list of lists) "
                                "of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for rw in matrix:
            new_row = []
            for item in rw:
                val = round(item / div, 2)
                new_row.append(val)
            new_matrix.append(new_row)
    return new_matrix
