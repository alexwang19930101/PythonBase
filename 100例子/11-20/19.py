#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sys import stdout

for j in xrange(2,1001):
    k = []
    s = j
    for i in xrange(1,j):
        if j % i == 0:
            k.append(i)
            s -= i
    if s == 0:
        print j
        for i in xrange(len(k)):
            print k[i],
        print