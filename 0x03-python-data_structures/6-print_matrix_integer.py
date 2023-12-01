#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for _row in matrix:
        for _column in _row:
            if _column == _row[-1]:
                print('{:d}'.format(_column), end='')
            else:
                print('{:d}'.format(_column), end=' ')
        print()
