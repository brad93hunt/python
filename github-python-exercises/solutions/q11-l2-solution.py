#!/usr/bin/env python
#
# Question 11 - Level 2
#
# Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

def main():

    value = []
    items=[x for x in raw_input().split(',')]

    for p in items:
        intp = int(p, 2)
        if not intp%5:
            value.append(p)

    print ','.join(value)

if __name__ == '__main__':
    main()
