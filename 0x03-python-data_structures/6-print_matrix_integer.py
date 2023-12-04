#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for l, item in enumerate(row):
            if l != 0:
                print(" ", end="")
            print("{:d}".format(item), end="")
        print()
