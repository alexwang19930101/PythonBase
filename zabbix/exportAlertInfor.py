#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xlwt
import os
import sys
import json
import datetime
from zbx_api import Apis

def getAlert():
    apis = Apis("10.127.2.49","admin","zabbix")
    res = apis.get_alerts("host-3","1507564800","1507623810")
    return res

def writeAlertIntoXml(alertInfo=""):
    #create workbook and sheet
    workbook = xlwt.Workbook()
    AlertInforSheet = workbook.add_sheet("AlertInforSheet", cell_overwrite_ok=True)
    
    #add Xtitle
    row0 = ["TRIGGER_NAME","HOST_NAME","TRIGGER_STATUS","TRIGGER_SEVERITY"]
    for i in xrange(len(row0)):
        AlertInforSheet.write(0,i,row0[i])
    
    #add alert information
    response = getAlert()
    alertResList = response['result']
#     print alertResList
    for i in xrange(len(alertResList)):
        messagelist = alertResList[i]['message'].split('*')
        for j in xrange(len(messagelist)):
            AlertInforSheet.write(i+1,j,messagelist[j])
    #save
    workbook.save("alertInformation(%s).xlsx" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
def main():
    writeAlertIntoXml()
    
if __name__ == "__main__":
    main()

