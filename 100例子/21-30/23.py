#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
打印
   *
  ***
 *****
*******
 *****
  ***
   *
'''

def rhombus(length):
    if (length-1)%2 != 0:
        print "error lenght"
    else:
        spaceNum = (length-1)/2
        asteriskNum = 1
        while asteriskNum < length:
            print(" "*spaceNum+"*"*asteriskNum)
            asteriskNum += 2
            spaceNum -= 1
        while asteriskNum > 0:
            print(" "*spaceNum+"*"*asteriskNum)
            asteriskNum -= 2
            spaceNum += 1

rhombus(7)