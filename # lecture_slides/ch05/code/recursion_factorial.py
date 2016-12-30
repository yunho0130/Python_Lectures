# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 06:08:45 2016

@author: Yunho
"""

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)
    
print factorial(3)