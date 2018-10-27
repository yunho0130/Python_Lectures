# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 07:33:25 2017

@author: Yunho
"""

def Main():
    queue = []           # queue create
    queue.append(1) # same PUT
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print queue

    while queue:
        print "GET > ",queue.pop(0) # same GET

Main()

