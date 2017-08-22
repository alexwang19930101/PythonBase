#-*- coding:utf8 -*-

class Cat:
    #属性
    def __init__(self,name="Cat"):
        self.name = name
    #方法
    def eat(self):
        print("%s eat" % self.name)
    
    def drink(self):
        print("%s drink"% self.name)
    
#创建对象
tom = Cat("tom")

#调用实例方法
tom.eat()
tom.drink()

#已有的修改
tom.name = "a"
#没有的添加
tom.age = 1

#多个实例
maoge = Cat()
maoge.name = "lanmao"
maoge.eat()