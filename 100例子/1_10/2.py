#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''

'''
1.if-elseif-else
有点蠢
'''

'''
x = int(raw_input("净利润："))

if x<=100000:
    bonus=x*0.1
    print u"奖金:",bonus,u"元"
elif 100001<x<=200000:
    bonus=10000+(x-100000)*0.075
    print u"奖金:",bonus,u"元"
elif 200001<x<=400000:
    bonus=10000+7500+(x-200000)*0.05
    print u"奖金:",bonus,u"元"
elif 400001<x<=600000:
    bonus=10000+7500+10000+(x-400000)*0.03
    print u"奖金:",bonus,u"元"
elif 600001<x<=1000000:
    bonus=10000+7500+10000+6000+(x-600000)*0.015
    print u"奖金:",bonus,u"元"
elif 600001<x<=1000000:
    bonus=10000+7500+10000+6000+6000+(x-600000)*0.01
    print u"奖金:",bonus,u"元"
'''

'''
2.利用列表保存后统一处理
注意列表排列顺序影响处理
'''

profitThreshold = [100, 60, 40, 20, 10,0]
profitRate = [0.001, 0.015, 0.03, 0.05, 0.075, 0.1]

x = float(raw_input("净利润(万元)："))
commission = 0
for i in xrange(6):
    if x > profitThreshold[i]:
        commission += (x - profitThreshold[i])*profitRate[i]
        x = profitThreshold[i]
print commission,"万元"
