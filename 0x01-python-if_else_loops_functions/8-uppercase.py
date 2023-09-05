#!/usr/bin/python3

def islower(c):
    asc = ord(c)
    if asc >= 97 and asc < 123:
        return (True)
    else:
        return (False)

def uppercase(str):
    for ch in str:
        if islower(ch):
            ch = ord(ch) - 32
            ch = chr(ch)
        print(ch, end="")
    else:
        print()
