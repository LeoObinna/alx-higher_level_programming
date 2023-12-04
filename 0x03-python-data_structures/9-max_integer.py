#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    maxi_num = my_list[0]
    for num in my_list[1:]:
        if num > maxi_num:
            maxi_num = num

    return maxi_num
