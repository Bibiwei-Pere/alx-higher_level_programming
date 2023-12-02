#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        lastnum = i
    for index, number in enumerate(my_list):
        if idx < 0:
            return my_list
        elif idx > lastnum:
            return my_list
        elif idx == index:
            my_list[index] = element
            return my_list
