#!/usr/bin/python3

"""It defines a class Square"""


class Square:
    """It represents a square"""

    def __init__(self, size):
        """It initializes a new square.

        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get/Set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """It returns the current area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """It prints the sqaure with the # character"""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
