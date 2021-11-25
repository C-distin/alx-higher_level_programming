#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        sum_weight = 0
        sum_value = 0
        for i in my_list:
            sum_weight += i[1]
            sum_value += i[0] * i[1]
        return sum_value / sum_weight
