# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 18:13:32 2017

@author: Yunho
"""

numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    assert n >= 0.0, 'Data should only contain positive values'
    total += n
print 'total is:', total


# 위의 코드와 동일하게 작동
print "=="*6

class AssertionError(Exception):
    def __str__(self):
        return 'Data should only contain positive values'

numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    # if n < 0.0: 을 사용할 것을 권장
    if not n >= 0.0: 
        raise AssertionError()
    total += n
print 'total is:', total

