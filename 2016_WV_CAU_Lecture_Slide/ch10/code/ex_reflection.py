# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 17:46:40 2017

@author: Yunho
"""

# Reflection Example

class MyClass:
     def Hello(self, sText):
             return 'Hello ' + sText

MyClass().Hello('Peter')
 
print getattr(globals()['MyClass'](), 'Hello')('Peter')