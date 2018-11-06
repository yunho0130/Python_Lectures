x = 50

def func(z=30):
    print 'x is', z
    z = z*2
    print 'Changed local x to', z

# func(x)
func(50)
func()
print 'x is still', x
