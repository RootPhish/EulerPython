#!/usr/bin/python

term = 2
previousterm = 1

result = 2

while term < 4000000:
    temp = term + previousterm
    previousterm = term
    term = temp
    if term % 2 == 0:
        result += term

print(result)
