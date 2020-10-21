#!/usr/bin/env python

import PIL from Image
import sys

def converter(*args):
    source = args[0]
    destination = args[1]
    im = Image.open(source).convert("RGB")
    im.save(destination, "png")

if __name__ == "__main__":
    if(sys.argv[1] == "--help"):
        print("Give path to the source JPG file and destination to save PNG file")
    else:
        converter(sys.argv[1], sys.argv[2])
        