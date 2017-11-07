#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''

'''

a = """6/24
18/24
3/24
10/48
14/24
11/24
48/48
7/24
12/48
8/24
0/48
10/24
1/48
0/24
21/48
28/48
29/48
0/24
14/24
15/24
5/24
24/24"""

b = a.split("\n")
print b

sum1=0#分子 
sum2=0#分母
sum = 0#记录条数
for i in xrange(len(b)):
    c = b[i].split("/")
#     print c
    sum1 += int(c[0])
    sum2 += int(c[1])
    sum += 1
#print sum1,sum2,sum




'''
变量作用域
'''
    
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
for i in range(3):
    print 'The num = %d' % num
    num += 1
    autofunc()