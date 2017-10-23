#/usr/bin/env python
#-*- coding: utf-8 -*-

'''
斐波那契数列。 
'''

'''
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''

def FibonacciGenerator(amount):
    list = [0,1]
    if amount < 1:
        print "error amount!"
        return []
    elif amount == 1:
        return [0]
    elif amount == 2:
        return list
    else:
        for i in xrange(2,amount):
            newNum = list[i-2] + list[i-1]
            list.append(newNum)
    return list

list = FibonacciGenerator(2)
print list