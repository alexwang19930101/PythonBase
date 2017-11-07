#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
求输入数字的平方，如果平方运算后小于 50 则退出。
'''

inputNum = float(raw_input("输入一个数:"))

def sqrtTest(inputNum):
    if inputNum**2<50:
        return
    else:
        return inputNum**2

print sqrtTest(inputNum)