#!/usr/bin/python
from math import floor,ceil,sqrt

def isprimenumber(value):
    if value == 1: return False
    for i in range(2, floor(sqrt(value)) + 1):
        if(value % i == 0):
            return False
    return True

def findprimefactors(value):
    result = []
    for i in range(2, floor(sqrt(value))):
        if isprimenumber(i):
            while value % i == 0:
                result.append(i)
                value = value / i
    return result

print(findprimefactors(600851475143))
