#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newer_list = []
    if my_list:
        for num in my_list:
            newer_list.append(False if num % 2 else True)
        return newer_list
