# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 07:17:12 2017

@author: Yunho
"""
import random

def bubble_sort(x):
	length = len(x)-1
	for i in range(length):
		for j in range(length-i):
			if x[j] > x[j+1]:
			    x[j], x[j+1] = x[j+1], x[j]
	return x

                
numList = [random.randint(1,100) for _ in range(10)]
print numList
print bubble_sort(numList)


