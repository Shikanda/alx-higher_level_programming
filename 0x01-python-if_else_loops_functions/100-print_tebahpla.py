#!/usr/bin/python3
for letter in range(25, -1, -1):
    caps = letter + ord('A')
    if letter % 2 == 1:
        caps += 32
    print("{:c}".format(caps), end="")
