#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

b = raw_input("输入一个数字:")
b = int(b)
print b

a = 1
for i in xrange(5):
    if b/10 == 0:
        break
    else:
        b /= 10
        a += 1
print a