#!/usr/bin/env python
# Write a script that asks for your first name, last name and year ofbirth (should be on one line)

name, surname, age = input("Enter your name, surname and age. ").split()

print("Name: {}, Surname: {}, Age: {}".format(name, surname, age))