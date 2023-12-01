#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.
    Args:
    m_a: A list of lists of integers or floats.
    m_b: A list of lists of integers or floats.
    Returns:
    A list of lists of integers or floats.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not isinstance(m_a, list) or not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for rw in m_a:
        for element in rw:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for rw in m_b:
        for element in rw:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrices must have compatible dimensions.")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_a[0])):
                value += m_a[i][k] * m_b[k][j]
            row.append(value)
        result.append(row)
    return result