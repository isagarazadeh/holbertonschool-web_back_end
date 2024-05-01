#!/usr/bin/env python3
"""Variable Annotations"""

#def fn(a, b):
#    return a + b
num = [a, b] 

num = list(map(float, num))

total = reduce(lambda a, b: a + b, num)

print(total)
