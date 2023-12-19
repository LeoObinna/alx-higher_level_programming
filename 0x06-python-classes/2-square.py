#!/bin/python3

"""It defines a class square"""


class Square:
    """It represents a square"""

    def __init__(self, size=0):
        """It initializes a new square.

        Args:
        size (int: The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
