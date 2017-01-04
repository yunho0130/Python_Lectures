# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 08:56:01 2017

@author: Yunho
"""

class NotAllowedUserName(Exception):
    def __str__(self):
        return "허용되지 않은 계정명입니다."

def register_nick(nick):
    # 비속어 닉네임
    if nick == '바보':
        raise NotAllowedUserName()
    # 음란한 닉네임
    elif nick == '19금':
        raise NotAllowedUserName()
    # 운영자 사칭
    elif nick == '운영자':
        raise NotAllowedUserName()
    else:
        print '계정이 생성되었습니다. 계정명은 {} 입니다.'.format(nick)

try:
#    register_nick('바보')
    register_nick('새로운 유저')
#    register_nick('19금')
except NotAllowedUserName as e:
    print e

    