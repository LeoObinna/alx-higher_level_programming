#!/usr/bin/python3
"""This module holds matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix representing the result of the division.
    Raises:
        if the matrix is empty or not a list
        if div is a number
        if div is not equal to 0
        if each row of the matrix has the same size

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " *
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " *
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in row:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " *
                                "of integers/floats")
    return [[round(y / div, 2) for y in row] for row in matrix]
