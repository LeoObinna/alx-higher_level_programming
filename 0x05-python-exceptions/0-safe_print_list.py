#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    for a in range(x):
        try:
            print(my_list[a], end="")
            number += 1
        except IndexError:
            break
    print("")
    return (number)
