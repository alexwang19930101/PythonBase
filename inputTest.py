#-*- coding:utf8 -*-
"""
while True:
    try:
        a = input("请输入a的值：")
        a = float(a)
        print type(a)
        break
    except:
        print "请输入数值，不要瞎搞！"
    finally:
        print "好智障"
"""

"""
workHours = float(input("输入工作时长："))
workRate = float(input("输入工作时薪："))
print workHours*workRate
"""
a=lambda x,y:x*y
print a(float(input("输入工作时长：")),float(input("输入工作时薪：")))
