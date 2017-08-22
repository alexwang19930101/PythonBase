#-*- coding:utf-8 -*-
def test(a,b=10):
    return a+b


print test(1,)
print test(b=1,a=2)


'''
#缺省参数只能放后面
def test1(a=1,b):
    return a+b
print test1(,1)
'''