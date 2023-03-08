#!/usr/bin/python3
def remove_char_at(str, n):
    the__str = ""
    for i, letter in enumerate(str):
        if i != n:
            the_str += letter
    return the_str
