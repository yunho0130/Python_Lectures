# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 22:19:11 2017

@author: Yunho
"""

import random
print random.random()

print random.randrange(1,7)

# 순서형자료를 섞는 역할
abc = ['a', 'b', 'c', 'd', 'e']
print abc
random.shuffle(abc)
print abc

# 재정렬 
abc.sort()
print abc

