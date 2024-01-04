#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: the first integer
        b: the second integer

    Raises:
        TypeError: if either of a or b is a non-integer and non-float.

    Returns:
        The addition of integer a and b.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
