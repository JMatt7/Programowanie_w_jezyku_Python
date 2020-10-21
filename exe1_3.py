#!/usr/bin/env python
import getpass


#Write a script that implements the code lock function. It asksfor the code and then checks if it matches the previously enteredcode

def passSetter():
    code, confCode = None, None

    while(True):
        code = getpass.getpass(prompt="Enter code: ")
        confCode = getpass.getpass("Confirm code: ")

        if(code != confCode):
            print("Code and confirmation code are not the same.")
        else:
            print("Code and confirmation code are the same. Your passcode is set.")
            break

if __name__ == "__main__":
    print("Hello enter the pin code and confirm with the same code for lock function.")
    passSetter()