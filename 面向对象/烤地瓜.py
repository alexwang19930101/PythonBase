#-*- coding:utf8 -*-

class Digua:

    def __init__(self, cookStr="生的",cookTotalTime=0, seasoning=[]):
        self.cookstr = cookStr
        self.cookTotalTime = cookTotalTime
        self.seasoning = seasoning
        
    def __str__(self):
        return "地瓜目前是"+self.cookstr+"，烤了"+str(self.cookTotalTime)+"分钟，加入佐料有"+str(self.seasoning)
    
    def cooking(self,cooktime):
        self.cookTotalTime += cooktime
        
        if self.cookTotalTime >= 5:
            self.cookstr = "熟的"
    
    def addSeasonig(self,seasoning):
        self.seasoning.append(seasoning)
        
digua = Digua()
digua.cooking(6)
digua.addSeasonig("大")
print digua


