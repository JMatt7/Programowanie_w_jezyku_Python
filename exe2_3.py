#!/usr/bin/env python

import sys
import os


def converter(*args):
    dirlist = os.listdir(os.getcwd())

    for i in range(0, len(dirlist)):
        if(dirlist[i].find('.jpg') != -1):
            os.rename(dirlist[i], dirlist[i][0:dirlist[i].find('.jpg')]+'.png')


if __name__ == "__main__":
    if(sys.argv[1] == "--help"):
        print("Give path to the source JPG file and destination to save PNG file")
    else:
        converter(sys.argv[1], sys.argv[2])
