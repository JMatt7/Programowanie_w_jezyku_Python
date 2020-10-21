#!/usr/bin/env python
from random import randint

def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

if __name__ == "__main__":
    arr = []
    for i in range(0, 50):
        arr.append(randint(1, 1000))
    test = arr
    quick_sort_recursion(arr, 0, len(arr) - 1)
    test.sort(reverse=True)
    for i in range(0, 50):
        print(test[i], " ", arr[i])
    
    print(test == arr)