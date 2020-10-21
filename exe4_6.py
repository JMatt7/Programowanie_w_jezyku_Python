#!/usr/bin/env python

from random import randint

def determinant(A):
    # Section 1: Establish n parameter and copy A
    n = len(A)
    AM = A
 
    try:
        for k in range(n): 
            for i in range(k+1,n): 
                if AM[k][k] == 0: 
                    AM[k][k] == 1.0e-18 
                crScaler = AM[i][k] / AM[k][k] 
                for j in range(n): 
                    AM[i][j] = AM[i][j] - crScaler * AM[k][j]
        
        product = 1.0
        for i in range(n):
            product *= AM[i][i] 
    except ZeroDivisionError:
        return 0
    return int(round(product))


if __name__ == "__main__":
    n = randint(2, 10)
    matrix1 = [[randint(0, 10) for i in range(0, n)] for j in range(0, n)]
    for x in matrix1:
        print(x)
    print("Determinant: ", determinant(matrix1))
