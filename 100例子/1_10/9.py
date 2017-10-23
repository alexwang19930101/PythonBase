#/usr/bin/env python
#-*- coding: utf-8 -*-

'''
暂停一秒输出。 
'''
import time

for i in xrange(5):
    print i
    time.sleep(1)
print 'end'