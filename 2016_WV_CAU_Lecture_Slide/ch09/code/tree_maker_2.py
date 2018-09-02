# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 07:21:40 2017

@author: Yunho
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:39:11 2016
@author: Yunho
"""
import sys

#print sys.argv[0] # prints python_script.py
#print sys.argv[1] # prints var1
#print sys.argv[2] # prints var2
print "ver 2.0"



def tree_maker(initial_num, increasing_tree, tree_space):
    shape = "*"
    space = " "
    space_num = initial_num
    initial_num = initial_num*2 -1
    print space * (2+tree_space - space_num) + shape * initial_num
    initial_num += increasing_tree
    print space * (1+tree_space - space_num) + shape * initial_num
    initial_num += increasing_tree
    print space * (0+tree_space - space_num) + shape * initial_num
    
def pot_maker():
    """Draw pot
    
    this is default function of tree"""
    pass
    
def main():
    """This is main function
    
    You can draw christmas tree using this module"""
#    help(tree_maker)
#    help(pot_maker)
    level_of_tree = int(sys.argv[1])
    tree_space = level_of_tree+5
    level_of_tree += 1
    for i in range(1,level_of_tree):
        tree_maker(i, 2, tree_space)
    
if __name__ == "__main__":
    main()