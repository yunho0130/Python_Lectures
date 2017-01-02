# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 06:32:36 2016

@author: Yunho
"""

a_list = [1, 9, 8, 4]
print([elem * 2 for elem in a_list])           #1
## [2, 18, 16, 8]
print(a_list)                                  #2
## [1, 9, 8, 4]
a_list = [elem * 2 for elem in a_list]         #3
print(a_list)
## [2, 18, 16, 8]