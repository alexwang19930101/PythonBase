#-*- coding:utf8 -*-

class Game(object):
    #类属性
    num = 0
    
    #类方法
    @classmethod
    def add_num(cls):
        cls.num += 1
        
    #实例方法
    def __init__(self):
        #实例属性
        self.name = "a"
        Game.add_num()
        #self.add_num()

    #静态方法
    @staticmethod
    def myStaticMethod():
        print "myStaticMethod"
game = Game()
print game.num
print Game.num

Game.myStaticMethod()
game.myStaticMethod()