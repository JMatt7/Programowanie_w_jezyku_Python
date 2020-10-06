#!/usr/bin/env python
import getpass


#Write a script that implements the code lock function. It asksfor the code and then checks if it matches the previously enteredcode


print("Hello enter the pin code and confirm with the same code for lock function.")
    
code, confCode = None, None

while(True):
    code = getpass.getpass(prompt="Enter code: ")
    confCode = getpass.getpass("Confirm code: ")

    if(code != confCode):
        print("Code and confirmation code are not the same.")
    else:
        print("Code and confirmation code are the same. Try again.")
        break
