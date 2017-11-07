#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
lambda函数
'''

MAXNUM = lambda x,y :(x>y)*x+(x<y)*y
MINNUM = lambda x,y :(x>y)*y+(x<y)*x

x = 10
y = 15
print MAXNUM(x,y)
print MINNUM(x,y)