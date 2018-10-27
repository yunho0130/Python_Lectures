__version__ = '0.1'

def hello_world():
    print 'hello world'

def say_hi():
    print 'hi'

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'
