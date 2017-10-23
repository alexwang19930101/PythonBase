#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
求一个3*3矩阵对角线元素之和。
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_ = 0
for i in range(0, 3):
    sum_ += matrix[i][i]
print sum_