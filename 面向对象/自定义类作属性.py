#-*- coding:utf8 -*-

class House:

    def __init__(self, areaTotal,location,item=[]):
        self.areaTotal = areaTotal
        self.areaFree = areaTotal
        self.location = location
        self.item = item
    
    def __str__(self):
        return "房屋在%s,总面积%s，可用面积%s" % (self.location,self.areaTotal,self.areaFree)
    
    def addItem(self,item):
        self.item.append(item)
        self.areaFree -= item.getArea()
        print "add item：%s" % item.getName()
        print "目前items：" 
        for itemIterator in self.item:
            print itemIterator

class Bed:

    def __init__(self, name, area):
        self.__name = name
        self.__area = area
    
    def __str__(self):
        return "    名称：%s,面积：%d" % (self.getName(),self.getArea())
    
    def getName(self):
        return self.__name
    
    def getArea(self):
        return self.__area
    
house = House(120,"武汉")
print house

bed = Bed("水床",4)
house.addItem(bed)
bed = Bed("席梦思",3.6)
house.addItem(bed)
print house
        