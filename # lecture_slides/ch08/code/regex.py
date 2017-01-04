# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 07:02:24 2017

@author: Yunho
"""

# Ref: 정두식 https://goo.gl/r4xz6m

# 따옴표(')로 둘러쌓인 부분에 원하는 정규표현식을 적습니다.
regex = r'[가-힣]+'

# 전화번호 0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}
# 숫자 \d
# 특수문자 제외한 문자 \w   (언더바는 포함)
#  \d+라고 쓰면 "하나 혹은 그 이상 연결된 숫자"
# 자연수 [1-9]\d*
# 전화번호에 - 여부와 상관없이 유효성 체크 \d+-?\d+-?\d+
# 전화번호 길이까지 지정해주는 정규식 \d{2,3}[- ]?\d{3,4}[- ]?\d{4}
# 영어 알파벳중에 소문자 모음(a,e,i,o,u)만 골라서 보고 싶을때 [aeiou]
# 영어 알파벳 소문자 전부 [a-z]
# 모든 한글 [가-힣]+
# \s 공백문자(스페이스, 탭, 뉴라인)
# \S 공백문자를 제외한 문자
# \D 숫자를 제외한 문자
# \W 글자 대표문자를 제외한 글자들(특수문자, 공백 등)


search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com ㅏㅇㄱㄱㅎ'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))

