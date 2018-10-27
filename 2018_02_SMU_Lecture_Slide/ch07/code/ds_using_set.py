# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 21:56:09 2017

@author: Yunho
"""

bri = set(['brazil', 'russia', 'india'])

print bri
print type(bri)

print 'india' in bri
print 'usa' in bri

bric = bri.copy() # frozen set이 아니기 때문에 mutable로 처리되어 deep copy 필요 
#bric = bri
bric.add('china')
bric.add('china') # 중복되는 값은 추가되지 않음
print bric.issuperset(bri)

bri.remove('russia')
print bri
print bric

print bri & bric

