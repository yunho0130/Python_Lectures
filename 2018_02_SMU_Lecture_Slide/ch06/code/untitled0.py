# -*- coding: utf-8 -*-

"""

Created on Tue Sep 18 16:25:52 2018



@author: HDC_USER

"""
print "Multiple Calculator"

def continue_check():
    print "Continue? 계속 하시겠습니까? "
    answer = raw_input("Y/N: ")
    if answer == "n":
        condition = False
    elif answer == "y": 
        pass
    else: 
        print "wrong answer 값을 잘못입력하셨습니다. 계산을 계속합니다."

def operator_check(num1, num2):
    operator = int(raw_input("1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈: "))
    if operator == 1:
        return num1+num2
    elif operator == 2: 
        pass
    elif operator == 3: 
        pass
    elif operator == 4: 
        pass
    else: 
        print "wrong answer 값을 잘못입력하셨습니다. 계산을 계속합니다."

condition = True

while condition:
    print "Input variables"
    num1 = int(raw_input("Input 1: "))
    num2 = int(raw_input("Input 2: "))
    # print int(num1)*int(num2)
    print operator_check(num1, num2)
    # continue_check()
    
# print "result: {}".format(int(input_val_1)*int(input_val_2))
        
