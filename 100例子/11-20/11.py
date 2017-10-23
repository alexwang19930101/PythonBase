#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ 
'''

global infantRabbit1,infantRabbit2,adultRabbit
def rabbitNumOneMonth(infantRabbit1,infantRabbit2,adultRabbit):
    adultRabbit = adultRabbit+infantRabbit2
    infantRabbit2 = infantRabbit1
    infantRabbit1 = adultRabbit
    return (infantRabbit1,infantRabbit2,adultRabbit)

def rabbitAmount(n):
    infantRabbit1 = 1
    infantRabbit2 = 0
    adultRabbit = 0
    for i in xrange(n-1):
        infantRabbit1,infantRabbit2,adultRabbit = rabbitNumOneMonth(infantRabbit1, infantRabbit2, adultRabbit)
    amount = 2*(infantRabbit1+infantRabbit2+adultRabbit)
    return amount

amount = rabbitAmount(16)
print "%s对" % (amount/2),"\r\n%s只" % amount