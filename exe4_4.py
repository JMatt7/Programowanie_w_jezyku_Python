#!/usr/bin/env python

from random import randint

def sum2Matrix(matrix1, matrix2):
    if(len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])):
        res = [[0 for i in range(0, len(matrix1))] for j in range(0, len(matrix1[0]))]
        for i in range(0, len(matrix1)):
            for j in range(0, len(matrix1[0])):
                res[i][j] = matrix1[i][j] + matrix2[i][j]
        return res
    else:
        raise "The matrix must be the same length!"

if __name__ == "__main__":
    matrix1 = [[randint(0, 100) for i in range(0, 128)] for j in range(0, 128)]
    matrix2 = [[randint(0, 100) for i in range(0, 128)] for j in range(0, 128)]

    res = sum2Matrix(matrix1, matrix2)
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1[0])):
            print(res[i][j], end=" ")
        print("")


    