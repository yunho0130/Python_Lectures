# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 08:27:41 2017

@author: Yunho
"""

class User(object):
    def __init__(self, input_name):
        self.hidden_name = input_name
        self.job = "초보자"
    def get_name(self):
        print "inside getter"
        return self.hidden_name
    def set_name(self, new_name):
        print "inside setter"
        self.hidden_name = new_name
    name = property(get_name, set_name)
    

    def skill_casting(self):
        print "{0} - {1}은/는 스킬을 시전합니다".format(self.hidden_name, self.job)
        if self.job =="초보자":
            print "초보자의 가호 버프가 시전됩니다. 피로도가 증가하지 않습니다."
    def attack(self):
        self.skill_casting()
        print "{}은/는 일반 공격을 합니다.".format(self.name)
    
class Knight(User):
    def __init__(self, input_name, level):
        User.__init__(self, input_name)
        self.job = "기사"
        self.level = level
    
    def knight_skill(self):
        self.skill_casting()
        if self.level <= 20:
            print "스킬 요구 레벨보다 낮아 스킬을 시전할 수 없습니다."
        elif self.level > 20:
            print "기사 1단계 스킬 '크리티컬 스트라이크' 발동합니다. 상대가 큰 타격을 받았습니다"

class Wizard(User):
    def __init__(self, input_name, level):
        User.__init__(self, input_name)
        self.job = "마법사"
        self.level = level
        
    def wizard_skill(self):
        self.skill_casting()
        if self.level <= 20:
            print "스킬 요구 레벨보다 낮아 스킬을 시전할 수 없습니다."
        elif self.level > 20:
            print "마법사 1단계 스킬 '파이어볼' 발동합니다. 상대가 큰 타격을 받았습니다"

class MagicalKnight(Knight, Wizard):
    def __init__(self, input_name, level):
        User.__init__(self, input_name)
        self.job = "마검사"
        self.level = level
    
    def magical_knight_skill(self):
        self.skill_casting()
        Knight.knight_skill(self)
        Wizard.wizard_skill(self)
        
        
def main():
    print "메인함수입니다."
    knight_1 = Knight("나는야기사",45)
    knight_1.knight_skill()
    wizard_1 = Wizard("나는야법사",45)
    wizard_1.wizard_skill()
    mkight_1 = MagicalKnight("나는야마검사", 45)
    mkight_1.magical_knight_skill()
    user_1 = User("나는야초보자")
    user_1.attack()
#    print user_1.__hidden_job # error
    
if __name__ == '__main__':
    main()
    
    
    