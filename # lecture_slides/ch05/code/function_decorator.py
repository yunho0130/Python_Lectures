# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime


def codeline_decorator(func):
    
    def nested_codeline():
        print '======코드 실행 시작======'
        func()
        print '======코드 실행 끝 ======='
    return nested_codeline

def timestamp_decorator(func):
    """Calculate function call running time. Use decorator
    
    import datetime module is required """
    
    print 'timestamp_decorator 내부', func.__name__

    def nested_timestamp():
        before_var_time = datetime.datetime.now()
        func()
        after_var_time = datetime.datetime.now() 
        print 'nested_timestamp 내부', func.__name__
        print "실행 시간은 다음과 같습니다"
        print before_var_time - after_var_time
    return nested_timestamp

# hello_world = timestamp_decorator(hello_world) 의 명료화
#@timestamp_decorator
def hello_world():
    """This function print 'hello world' string

    This function is just a test script for confirm of installation"""
    print '헬로 월드'
    print 'hello'+'world'

@codeline_decorator
def unicode_practice():
    # 유니코드 관련
    print "안녕하세요"
    print len("안녕하세요")
    print len(u"안녕하세요")

def main():
    """Main Function

    This function is main function.
    All functions what you want to implement should called by this function."""

    unicode_practice()
    
if __name__ == "__main__":
    main()

