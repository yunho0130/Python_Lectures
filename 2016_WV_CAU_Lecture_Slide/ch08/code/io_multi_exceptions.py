# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 08:46:48 2017

@author: Yunho
"""

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")