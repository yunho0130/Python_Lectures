# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 07:24:30 2017

@author: Yunho
"""

class User(object):
    def __init__(self, input_name):
        self.hidden_name = input_name
        
    def account_info(self):
        print "일반유저 입니다." 
        print "닉네임은 다음과 같습니다."
        print self.hidden_name
        
    def get_name(self):
        print "inside getter"
        return self.hidden_name
    def set_name(self, new_name):
        print "inside setter"
        self.hidden_name = new_name
    name = property(get_name, set_name)

class Admin(User):
    def __init__(self, input_name, admin_grade):
        User.__init__(self, input_name)
        self.admin_grade = admin_grade
    
    # method overriding
    def account_info(self):
        print "운영진 입니다."
        print "운영진 등급은 {} 입니다".format(self.admin_grade)
        print "운영진 닉네임은 {} 입니다.".format(self.hidden_name)

    # like method overloading
    def notice(self, message, id=None):
        if id == None:
            print "전체공지를 합니다." 
            print "[전체] {}".format(message)
        else:
            print "개별 공지를 합니다." 
            print "[개별] {}".format(message), id

# error
#    def notice(self, message, num):
#        print "반복 전체 공지를 합니다." 
#        print "[전체] {}".format(message)

        
def main():
    print "메인함수"
    user_1 = User('yunho0130')
    user_1.account_info()
    
    admin_1 = Admin('myh0130', 'Operator')
    admin_1.account_info()
    
    admin_1.notice('버그나 핵 사용자는 계정이 삭제됩니다')
    admin_1.notice('당신의 계정이 버그를 사용하는 것으로 시스템이 감지했습니다', 'myh0130')

if __name__ == '__main__':
    main()
    
