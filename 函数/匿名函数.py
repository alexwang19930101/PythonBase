#-*- coding:utf-8 -*-

#匿名函数默认自带return   lambda 参数：式子
#a = lambda x,y:x+y
#print a(1,2)

'''
#应用
infors = [{"a":1,"age":19},{"b":2,"age":18},{"c":3,"age":20}]

infors.sort(key = lambda x:x['age'])
print infors

def test(a,b,func):
    result = func(a,b)
    print(result)

test(11,22,lambda x,y:x*y)

func_new = input("输入：")
test(11,22,func_new)
'''
a1=1
b1=2

a1,b1 = b1,a1

print a1,b1 