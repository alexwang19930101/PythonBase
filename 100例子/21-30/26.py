#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
题目：利用递归方法求5!。
'''

def mul(n):
    if n == 1:
        return 1
    else:
        return n*mul(n-1)

print mul(5)