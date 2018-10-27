# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 21:44:02 2017

@author: Yunho
"""
# Google Python 권장사항
from module_using_name import say_hi 
say_hi()

# import 문으로만 사용도 가능함
import module_using_name
module_using_name.say_hi()
module_using_name.hello_world()

print module_using_name.__version__