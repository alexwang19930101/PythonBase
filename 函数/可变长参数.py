#-*- coding:utf-8 -*-
from test.test_array import ArraySubclassWithKwargs

#只能放最后面
def sum2nums(a,*args):
    if len(args)>0:
        for num in args:
            a += num
    return a

print sum2nums(1,2,3)
print sum2nums(1)

def testKW(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)

testKW(1,2,3,key='value')

A=(11,)
B={'key':'value'}
testKW(11,A,B)
testKW(11,*A,**B)