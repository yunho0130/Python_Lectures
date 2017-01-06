# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 07:35:43 2017

@author: Yunho
"""
import random

def quicksort(x):
    if len(x) <= 1:
        return x
    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)

numList = [random.randint(1,100) for _ in range(10)]
print numList
print quicksort(numList)

