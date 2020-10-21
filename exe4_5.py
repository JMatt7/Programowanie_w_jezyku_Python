#!/usr/bin/env python

from random import randint

def mult2Matrix(matrix1, matrix2):

    if(len(matrix1[0]) == len(matrix2)):
        res = [[0 for i in range(0, len(matrix2[0]))] for j in range(0, len(matrix1))]
        for i in range(0, len(matrix1)):
            for j in range(0, len(matrix2[0])):
                for k in range(0, len(matrix2)):
                    res[i][j] += matrix1[i][k] * matrix2[k][j]
        return res
    else:
        raise "The numbers of rows in firs matrix must be the same as the numbers of rows in second matrix!"
    
if __name__ == "__main__":
    matrix1 = [[randint(0, 10) for i in range(0, 8)] for j in range(0, 8)]
    matrix2 = [[randint(0, 10) for i in range(0, 8)] for j in range(0, 8)]
    print(len(matrix2))
    res = mult2Matrix(matrix1, matrix2)
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2[0])):
            print(res[i][j], end=" ")
        print("")
