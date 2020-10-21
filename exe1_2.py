#!/usr/bin/env python
# Write a script that asks for your first name, last name and year ofbirth (should be on one line)

def printInfo(name, surname, age):
    print("Name: {}, Surname: {}, Age: {}".format(name, surname, age))

if __name__ == "__main__":
    name, surname, age = input("Enter your name, surname and age. ").split()
    printInfo(name, surname, age)