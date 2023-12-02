#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        lastnum = i
    for index, element in enumerate(my_list):
        if idx < 0:
            return None
        elif idx > lastnum:
            return None
        elif idx == index:
            return element
