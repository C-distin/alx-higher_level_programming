#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = set()
    for i in zip(set_1, set_2):
        if i[0] == i[1]:
            c_set.add(i[0])
    return c_set
