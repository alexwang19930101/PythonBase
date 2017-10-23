#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
求出这个数列的前20项之和。
'''

def numGenerator(list,amount):
    for i in xrange(2,amount):
        newNum = list[i-2] + list[i-1]
        list.append(newNum)
    return list

numeratorList = numGenerator([2.0,3.0],20)
denominatorList = numGenerator([1.0,2.0],20)
sum = 0

for i in xrange(20):
    sum += numeratorList[i]/denominatorList[i]
print sum