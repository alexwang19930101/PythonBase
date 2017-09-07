#-*- coding:utf-8 -*-

class Person(object):
    """人的类"""
    def __init__(self,name):
        super(Person, self).__init__()
        self.name = name
        self.hp = 100
        self.gun = None
        
    def magazineCharge(self,magazine,bullet):
        magazine.magazineCharge(bullet)
    
    def mountMagazine(self,gun,magazine):
        gun.mountMagazine(magazine)
        
    def holdGun(self,gun):
        self.gun = gun
        
    def shoot(self,person):
        if self.gun:
            person.hp -= 10
        
class Gun(object):
    """枪的类"""
    def __init__(self,type):
        super(Gun, self).__init__()
        self.type = type
        self.magazine = None
        
    def mountMagazine(self,magazine):
        self.magazine = magazine
        
class Magazine(object):
    """弹夹"""
    def __init__(self,magazineSize):
        super(Magazine, self).__init__()
        self.magazineSize = magazineSize
        self.bulletList = []
        
    def magazineCharge(self,bullet):
        self.bulletList.append(bullet)
        
class Bullet(object):
    """子弹"""
    def __init__(self,type):
        super(Bullet, self).__init__()
        self.type = type
        
def main():
    """程序流程"""
    pass

    #1.创建持枪者
    print "laowang created"
    laowang = Person("laowang")
    #2.创建枪
    print "gun created"
    gun = Gun("M32")
    #3.创建弹夹
    print "magazine(20) created"
    magazine = Magazine(20)
    #4.创建子弹
    for i in xrange(20):
        print "bullet(%s) created" % i
        bullet = Bullet("10")
        #5.老王装弹
        print "laowang charged magazine %s" % i
        laowang.magazineCharge(magazine, bullet)
    #7.弹夹入枪
    print "put magazine in gun"
    laowang.mountMagazine(gun, magazine)
    #6.创建敌人
    enemy = Person("enemy")


    #8.持枪对敌
    laowang.holdGun(gun)
    #9.开枪
    laowang.shoot(enemy)
    print enemy.hp
    laowang.shoot(enemy)
    print enemy.hp
    
if __name__ == "__main__":
    main()