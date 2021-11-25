#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    return {key: value * 2 for key, value in new_dict.items()}
