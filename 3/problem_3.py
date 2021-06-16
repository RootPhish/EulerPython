#!/usr/bin/python
from math import floor,ceil,sqrt

def isprimenumber(value):
    if value == 1: return False
    for i in range(2, floor(sqrt(value)) + 1):
        if(value % i == 0):
            return False
    return True

def primenumbersupto(value):
    result = []
    for i in range(2, value):
        if isprimenumber(i):
            result.append(i)
    return result

def findprimefactors(value):
    result = []
    primes = primenumbersupto(floor(sqrt(value)))
    for prime in primes:
        while value % prime == 0:
            result.append(prime)
            value = value / prime
    return result

print(findprimefactors(600851475143))
