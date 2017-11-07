#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
两个变量值互换。
'''
'''
方法一，交叉返回
'''

def exchangeValue1(a,b):
    return b,a

'''
方法二，计算局部变量后返回
'''
def exchangeValue2(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b


a = 10
b = 9
a,b = exchangeValue2(a, b)
print a,b


