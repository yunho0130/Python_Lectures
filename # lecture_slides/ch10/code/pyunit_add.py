# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 06:38:21 2017

@author: Yunho
"""

import unittest
from add import *

class TestAll(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(1,3), add(3,1))
 
if __name__ == '__main__':
    
# unittest.main() 함수는 현재 모듈 안에 있는 
# 모든 testXXX 형식의 함수를 찾아서 테스트를 수행한다.
    unittest.main()
    
    