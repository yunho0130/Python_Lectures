# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 07:34:57 2017

@author: Yunho
"""
import csv
# 한글 csv 파일 읽기
with open('./file.csv', 'rt') as csvfile: 
    reader = csv.reader(csvfile, delimiter=',') 
    for row in reader: 
        print " "
        for r in row:
            print r.decode('euckr').encode('utf-8'),

# 예외처리 ver            
import csv
import sys
filename = 'file.csv'
f = open(filename, 'rb')
reader = csv.reader(f)
try:
    for row in reader: 
        for r in row:
            print r.decode('euckr').encode('utf-8')
        
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
f.close() 

