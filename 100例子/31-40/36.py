#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
求100之内的素数。
'''

a = []

for i in xrange(2,101):
    flag = 1
    for j in xrange(2,i/2+1):
        if i%j == 0:
            flag = 0
            break
    if flag == 1:
        a.append(i)
print a,len(a)