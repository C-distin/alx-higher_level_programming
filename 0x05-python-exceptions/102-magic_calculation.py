#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += i * b
        except Exception as e:
            print("Exception: {}".format(e), end="")
            result = a + b
            break
    return result
