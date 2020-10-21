#!/usr/bin/env python
import sys
import math
def quadraticEquationSolver(a, b, c):
    d = b**2 - 4*a*c
    x1 = None
    x2 = None
    if d < 0: 
        print("First Solution: {} + {}i Second Solution {} - {}i".format((-b)/(2*a), math.sqrt(abs(d))/(2*a), (-b)/(2*a), math.sqrt(abs(d))/(2*a)))
    elif d > 0:
        x1 = (-b - math.sqrt(d))/(2*a)
        x2 = (-b + math.sqrt(d))/(2*a)
        print("First Solution: {} Second Solution {}".format(x1, x2))
    else:
        x1 = x2 = (-b)/(2*a)
        print("First Solution and Second Solution are the same {}".format(x1))


if __name__ == "__main__":
    quadraticEquationSolver(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        