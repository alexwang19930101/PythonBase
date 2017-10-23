#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''
l = []
flag = 1
for x in xrange(100,201):
    floor = 2
    ceiling = int(x**0.5)
    
    for i in xrange(floor,ceiling+1):
        if x % i == 0:
            flag = 0
            break
        
    if flag==1:
        l.append(x)
    flag = 1
print l