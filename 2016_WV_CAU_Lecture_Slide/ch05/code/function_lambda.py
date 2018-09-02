# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 07:25:14 2016

@author: Yunho
"""

def hap(x, y):
    
    return x + y
 
def main():
    print hap(10, 20) # 30

    # lambda 인자 : 표현식
    print (lambda x,y: x + y)(10, 20) # 30
    
    # map(함수, 리스트)
    print map(lambda x: x ** 2, range(5)) # [0, 1, 4, 9, 16]

    # filter(함수, 리스트)
    print filter(lambda x: x < 5, range(10)) 
    # [0, 1, 2, 3, 4]
    print filter(lambda x: x % 2, range(10)) 
    # 홀수 [1, 3, 5, 7, 9]  

if __name__ == "__main__":
    main()
