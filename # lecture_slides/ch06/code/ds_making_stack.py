# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 07:24:38 2017

@author: Yunho
"""

def main():
    stack = []            # stack create
    stack.append(1)  # same PUSH
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print stack

    while stack:
       print "POP >", stack.pop()

if __name__ == '__main__':
    main()
    
    