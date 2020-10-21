#!/usr/bin/env python
# Write a script that counts the number of files in the/devdirectory,use the standard library

import os

def filesCount(dire, inNum):
    while(inNum != 1 and inNum != 2):
        inNum = int(input())

    if inNum == 1:
        list = os.listdir(dire) 
        number_files = len(list)
        print("Numbers of files and subdirectories: ", number_files)
    if inNum == 2:
        onlyfiles = next(os.walk(dire))[2]
        print("Numbers of files: ", len(onlyfiles))


if __name__ == "__main__":
    print("Input directory to the files.")
    dire = input()
    print("If you want to count subdirectories and files enter 1. If only files enter 2.")
    inNum = None
    filesCount(dire, inNum)