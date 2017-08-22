#-*- coding:utf-8 -*-

#string不可变
'''
a = "hello"
a[0] = 'H'
'''

#tuple不可变
'''
a = (11,22)
a[0] = 1
'''
#字典、列表可变
a = [11,22]
a[0] = 1

#key是不可变类型
dir = {'a':'b','11':'a'}
dir['a'] = 'c'
print dir