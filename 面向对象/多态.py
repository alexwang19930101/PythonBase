#-*- coding:utf8 -*-

class Dog:
    def shout(self):
        print "dog bark"
        
class Tiger:
    def shout(self):
        print "tiger shout"
        
def show(obj):
    obj.shout()

dog = Dog()
tiger = Tiger()
show(dog)
show(tiger)