#-*- coding:utf-8 -*-

class Dog:
    def __init__(self,age=0):
        self.__age = age
    
    def setAge(self,age):
        if not isinstance(age, int):
            print "类型不正确！"
        else:
            if age>0 and age<100:
                self.__age = age
            else:
                print "这只狗修仙了"
    
    def __del__(self):
        pass
    
    def getAge(self):
        return self.__age
    
    def __isFull(self):
        print "full"
    
    def eat(self,isFull=False):
        if isFull == True:
            self.__isFull()
    
dog = Dog()
print dog.getAge()
dog.setAge(10)
print dog.getAge()
dog.setAge(100)
dog.setAge("1s")
dog.eat(True)