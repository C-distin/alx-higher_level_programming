#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index_row in matrix:
        print(" ".join("{:d}" .format(item) for item in index_row))
