#!/usr/bin/python

def isgood(value):
    for i in range(2, 21):
        if value % i != 0:
            return False
    return True
        
curnumber = 2520
while not isgood(curnumber):
    curnumber = curnumber + 1

print(curnumber)
