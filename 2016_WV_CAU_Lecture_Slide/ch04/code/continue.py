print "ver 1.2"
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print 'Too small'
        print 'continue expression before'
        continue
        print 'continue expression after'
    print 'Input is of sufficient length'
    # Do other kinds of processing here...
