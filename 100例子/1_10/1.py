#!/usr/bin/env python
#-*- coding: utf-8 -*-

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

'''
一般3重for循环
'''
'''
numList = [num for num in xrange(1,5)]
resultList = []

for i in numList:
    for j in numList:
        if i == j:
            continue
        for k in numList:
            if k == i or k == j:
                continue
            resultList.append("%d%d%d" % (i,j,k))

print len(resultList)
print resultList
'''

'''
列表生成式
'''
'''
numList = [1,2,3,4]
resultList = [i*100+j*10+k for i in numList for j in numList for k in numList if (i!=j and i!=k and j!=k)]
print len(resultList)
print resultList
'''

'''
使用自带排列函数permutations
问题：返回为元组,需要整理输出格式
'''
'''
from itertools import permutations

totalNum=0
for i in permutations(xrange(1,5),3):
    print "%d%d%d" % (i[0],i[1],i[2])
    totalNum += 1
print totalNum
'''