#/usr/bin/env python
#-*- coding: utf-8 -*-

'''
暂停一秒输出格式化当前时间。 
'''
import time

for i in xrange(5):
    print time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(time.time()))
    time.sleep(1)
print 'end'