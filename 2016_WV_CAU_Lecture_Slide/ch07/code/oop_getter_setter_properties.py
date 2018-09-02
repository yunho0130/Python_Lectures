# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 06:36:18 2017

@author: Yunho
"""

class User(object):
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print "inside getter"
        return self.hidden_name
    def set_name(self, new_name):
        print "inside setter"
        self.hidden_name = new_name
    name = property(get_name, set_name)

class Monster(object):
    def __init__(self, input_name):
        # name mangling 
        self.__real_hidden_name = input_name
    @property
    def name(self):
        print "inside getter(monster)"
        return self.__real_hidden_name
    @name.setter
    def name(self, new_name):
        print "inside setter(monster)"
        self.__real_hidden_name = new_name


def main():
    print "main 함수"
    user_1 = User('멍멍이')
    print user_1.hidden_name
    print user_1.get_name()
    user_1.set_name('야옹이')
    print user_1.get_name()
    print user_1.name
    user_1.name = '멍멍이'
    print user_1.name
    
    mon_1 = Monster('크고 무서운 래서팬더')
    print mon_1.name
    mon_1.name = '귀여운 래서팬더'
    print mon_1.name
#    mon_1.__real_hidden_name # error

if __name__ == '__main__':
    main()
    
