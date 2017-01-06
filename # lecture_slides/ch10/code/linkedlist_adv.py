# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 07:51:06 2017

@author: Yunho
"""

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [' +str(current.value) 
            while current.next != None:
                current = current.next
                out += str(current.value)+" "
            return out+']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

        
def main():
    L = LinkedList()
    L.insert(1)
    L.insert(1)
    L.insert(2)
    L.insert(4)
    print L
    L.clear()
    print L
    
    
    # Collections를 이용한 방법
    from collections import deque
    d = deque([1,2,3,4])
    
    print d
    for x in d:
        print x
    print d.pop(), d
    d.append(5)
    print d.pop(), d
    d.clear
    print d.pop(), d

if __name__ == '__main__':
    main()
    
    
    