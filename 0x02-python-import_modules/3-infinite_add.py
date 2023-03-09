#!/usr/bin/python3
if __name__ == "__main__":
    import sys

answer = 0

for i in range(1, len(sys.agrv)):
    answer += int(sys.agrv[i])
print("{:d}".format(answer))
