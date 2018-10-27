# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 07:27:11 2017

@author: Yunho
"""

f = open("poem.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

