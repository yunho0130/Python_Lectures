# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 06:29:57 2017

@author: Yunho
"""

oldlist = [1, 1, 2, 3, 3, 4]
 
newlist = {i*i for i in oldlist}
 
print(newlist)
# 출력 : {16, 1, 9, 4}

