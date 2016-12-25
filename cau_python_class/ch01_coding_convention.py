# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 00:16:09 2016

@author: Yunho
"""

# semicolons
# No 두 줄을 한 줄로 만드는 ; 사용하지 말 것
print "hello"; print "world"

# Statements - 1줄에 1개의 statement가 원칙

# No 끝나는 부분 수직열 맞출 필요 없음.
str1  =        'hello'
str24 =  'world world'

# Yes
str1='hello'
str24='world world'


# Line length

# No
print "hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello"

# Yes1
str = ('This will build a very long long '
     'long long long long long long string')
print str

# Yes2
if (width == 0 and height == 0 and
    color == 'red' and emphasis == 'strong'):

# Yes3 - long URLs은 길게 써도 무관 
# See details at
# https://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html

# Block and Inline Comments
# No - 코드 끝에 주석을 다는 경우는 자제하라. 위에 주석을 첨부하라. 
print "hello world" # This will build a very long long comments
# Yes - 공백 2칸뒤, 짧은 주석
print "hello world"  # Short comments
