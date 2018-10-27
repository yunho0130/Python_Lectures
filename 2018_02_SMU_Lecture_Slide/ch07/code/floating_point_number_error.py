# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 20:11:29 2017

@author: Yunho
"""

def timestamp_decorator(func):
    """Calculate function call running time. Use decorator
    
    import datetime module is required """
    
    import datetime
    print 'timestamp_decorator 내부', func.__name__

    def nested_timestamp():
        before_var_time = datetime.datetime.now()
        for i in range(1,1001):
            func()
            print i, '회 실행'
        after_var_time = datetime.datetime.now() 
        print 'nested_timestamp 내부', func.__name__
        print "실행 시간은 다음과 같습니다"
        print after_var_time - before_var_time
    return nested_timestamp

    
@timestamp_decorator
def main():
    
    # 기본 floating point 활용
    i = 0.1
    boolean_status = True
    
    while boolean_status:
        print i
        i += 0.1
        if i == 2:
            boolean_status = False
    
    # 오류를 보정한 decimal 자료형 활용
    boolean_status = True
    
    import decimal 
    import sys
    dcimal_i = decimal.Decimal('0.1')
    dcimal_j = decimal.Decimal('0.1')
    
    while boolean_status:
        print dcimal_i
        dcimal_i += dcimal_j
        if dcimal_i == 2:
            boolean_status = False
    
    print '=='*6
    print 'i'
    print type(i)
    print sys.getsizeof(i)
    print '=='*6
    print 'dcimal_i'
    print type(dcimal_i)
    print sys.getsizeof(dcimal_i) # 일반적인 float형에 비해 3배의 공간을 필요


if __name__ == '__main__':
    main()

