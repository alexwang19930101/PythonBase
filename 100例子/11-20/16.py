#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
输出指定格式的日期。
'''

import time
from datetime import datetime
#import  datetime

print time.ctime()

#datetime tuple
print datetime.now()

#time Timestamp
print time.time()

"""
string --> 其他
"""

date_str = "2010-1-1 10:10:10"
dt_obj_from_str = datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
print dt_obj_from_str

tm_obj = time.strptime(date_str,"%Y-%m-%d %H:%M:%S")
print tm_obj

"""
datetime obj转换为其它
"""
dt_obj = datetime(2008, 11, 10, 17, 53, 59)

date_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
print date_str
time_tuple = dt_obj.timetuple()
print time_tuple

"""
time obj转换为其它
"""
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)

time_str = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print time_str

dt_str = datetime(*time_tuple[0:6])
print dt_str

ts = time.mktime(time_tuple)
print ts

dt_fromts = datetime.fromtimestamp(ts)
print dt_fromts
tt_fromts = time.localtime(ts)
print tt_fromts
