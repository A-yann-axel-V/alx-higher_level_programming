#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for k, row in enumerate(matrix):
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
        print()
print_matrix_integer([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])