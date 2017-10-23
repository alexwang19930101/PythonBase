#/usr/bin/env python
#-*- coding: utf-8 -*-

'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''

l = []
for i in xrange(3):
    x = int(raw_input("请输入第%s个整数:" % (i+1)))
    #print type(x)
    l.append(x)
l.sort(cmp=None, key=None, reverse=False)
print l