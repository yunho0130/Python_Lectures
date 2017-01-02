# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 22:46:47 2017

@author: Yunho
"""

address_book = { '맹윤호':['010-2815-9190','yunho0130@gmail.com'] }
address_book['홍길동'] = ['010-1234-4567', 'hgd0130@gmail.com']

print address_book


for i,j in address_book.items():
    print i,':', j[0],',',j[1]