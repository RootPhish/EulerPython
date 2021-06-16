#!/usr/bin/python

max = 0

for i in range(1, 1000):
    for j in range(1, 1000):
        product = i * j
        prodstr = str(product)
        if product > max:
            if prodstr == prodstr[::-1]:
                max = product

print(max)
