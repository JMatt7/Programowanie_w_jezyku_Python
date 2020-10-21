#!/usr/bin/env python

def scalarValueOf2Vector(vec1, vec2):
    if len(vec1) == len(vec2):
        res = 0
        for i in range(0, len(vec1)):
            res += vec1[i] * vec2[i]
        return res
    else:
        raise "The vectors must be the same length!"


if __name__ == "__main__":
    vec1 = [1, 2, 12, 4]
    vec2 = [2, 4, 2, 8]
    print(scalarValueOf2Vector(vec1, vec2))
