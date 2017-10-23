#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''
l=[]
for i in xrange(100,1000):
    hundred = i/100
    decade = i/10 % 10
    unit = i%10
    if hundred**3 + decade**3 + unit**3 == i:
        l.append(i)
print l