#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list
    for i in new_list:
        lastnum = i
    for index, number in enumerate(new_list):
        if idx < 0:
            return new_list
        elif idx > lastnum:
            return new_list
        elif idx == index:
            new_list[index] = element
            return my_list[::-1]

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)