#/usr/bin/env python
#-*- coding: utf8 -*-

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

import time

inputTime = raw_input("输入年月日（%Y-%m-%d）:")
print(time.strptime(inputTime, '%Y-%m-%d')[7])