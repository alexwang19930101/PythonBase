#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
#注意hei为float
def dropBall(hei,tim):
    tour = []
    height = []
    
    for i in xrange(1,tim+1):
        if i == 1:
            tour.append(hei)
        else:
            tour.append(hei*2)
        hei /= 2
        height.append(hei)
    return tour,height

tour,height = dropBall(100.0, 10)
print sum(tour)
print height[-1]