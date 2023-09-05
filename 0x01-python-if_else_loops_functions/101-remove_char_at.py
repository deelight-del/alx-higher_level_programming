#!/usr/bin/python3

def remove_char_at(string, n):
    new_str = ""
    for index, char in enumerate(string):
        if index == n:
            continue
        else:
            new_str = new_str + char
    return new_str
