#!/usr/bin/python3
"""
The Module for Print_Square method"""


def print_square(size):
    """printing a square with # characters.

    Args:
        size: The int size of the square's side.

    Raises:
        TypeError: if size is not an integer"
        ValueError: if size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")
