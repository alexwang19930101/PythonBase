#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加由键盘控制。

'''

n = int(raw_input("输入一个整数:"))
a = 5
sum = 0
for i in xrange(1,n+1):
    sum += a*i*10**(n-i)
print sum