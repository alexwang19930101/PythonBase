#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

def palindromicNum(numStr):
    for i in xrange(len(numStr)/2):
        if numStr[i] != numStr[-1-i]:
            return False
    return True

palindromic1 = "12322"
palindromic2 = "12321"
print palindromicNum(palindromic1)
print palindromicNum(palindromic2)