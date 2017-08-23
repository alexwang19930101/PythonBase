#-*- coding:utf8 -*-

class Animal:
    def __init__(self,shape="体形"):
        self.shape = shape
    
    def run(self):
        print "animal run"
    def eat(self):
        print "animal eat"
    
    def __privateMethod(self):
        print "private"

    def showPrivate(self):
        self.__privateMethod()
        
class Dog(Animal):
    def shout(self):
        print "dog shout"
        
class Husky(Dog):
    def shout(self):
        print "Husky shout"
#A.method(self,arg)                #1  
#super(B, self).method(arg)        #2  
#super().method(arg)               #3
        
animal= Animal()
dog = Dog()
husky = Husky()

dog.eat()
dog.shout()
husky.shout()
#dog.__privateMethod()
dog.showPrivate()
