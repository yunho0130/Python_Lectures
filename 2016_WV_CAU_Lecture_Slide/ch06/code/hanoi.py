# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 17:46:04 2017

@author: Yunho
"""

def hanoi(num_disks, start_peg, temp_peg ,end_peg):
    if num_disks == 1:
        print '{} -> {}'.format(start_peg, end_peg)
    else:
        hanoi(num_disks-1, start_peg, end_peg, temp_peg) # 섞기
        hanoi(1, start_peg, temp_peg, end_peg) # 출력라인 
        hanoi(num_disks-1, temp_peg, start_peg, end_peg) # 섞기

def main():
    hanoi(3, 'A', 'B', 'C')

if __name__ == "__main__":
    main()        