#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sk = sorted(a_dictionary)
    for k in sk:
        print("{}: {}".format(k, a_dictionary[k]))
