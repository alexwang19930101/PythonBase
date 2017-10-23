#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

a = [1, 3, 4, 8, 12, 25, 34, 46, 75]
b = 11

def binaryInsert(a,b):
    fontPoint = 0
    endPoint = len(a)
    midPoint = (fontPoint+endPoint+1)/2
    while midPoint != endPoint:
        if b <= a[midPoint]:
            endPoint = midPoint
            midPoint= (fontPoint+endPoint+1)/2 
        else:
            fontPoint = midPoint
            midPoint= (fontPoint+endPoint+1)/2
    print midPoint
    a.append(0)
    i = len(a)-1
    while i > midPoint:
        a[i]=a[i-1]
        i -= 1
    a[midPoint] = b
    return a

print binaryInsert(a, b)
        