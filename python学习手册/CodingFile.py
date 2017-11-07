#!/usr/bin/env python
#-*- coding: utf-8 -*-
# y=95
# x = y // 2
# while x>1:
#     if y%x == 0:
#         print(y,'has factor',x)
#         break
#     x -= 1
# else: 
#     print(y,'is prime')

f = open('script1.py')
print f.readlines()
f.close()

f = open('script1.py')
print f.readline(),
print f.next(),
f.close()

for line in open('script1.py'):
    print(line,)

lines = [line.rstrip() for line in open('script1.py').readlines()]
print lines