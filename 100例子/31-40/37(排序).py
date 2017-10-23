#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
对10个数进行排序。
'''

def bubbleSort(a):
    for i in xrange(len(a)):
        for j in xrange(len(a)-i):
            if j<len(a)-1 and a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a

a = [1,3,25,4,75,12,46,34,8]

print bubbleSort(a)