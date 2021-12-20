#!/usr/bin/python3
def matrix_divided(matrix, div):
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    i = []
    j = []
    for x in matrix:
        if isinstance(x, list) is False:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(x) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for y in x:
            if isinstance(y, (int, float)) is False:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            i.append(y)
        j.append(x)
    if len(i) != len(j):
        raise TypeError("Each row of the matrix must have the same size")
    if len(i) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(j) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for x in j:
        if len(x) != len(j[0]):
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(x / div, 2) for x in y] for y in matrix]
