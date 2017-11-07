#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
'''

x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

resultMatrix = []

for i in xrange(len(x)):
    resultMatrix.append([])
    for j in xrange(len(x[i])):
        resultMatrix[i].append(x[i][j]+y[i][j])
print resultMatrix