#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

def recurion(str,n):
    if n == 0:
        pass
    else:
        recurion(str, n-1)
        print str[len(str)-n]

str = raw_input("请输入一个string:")
recurion(str, len(str))