#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xlwt
import os
import sys
import json

from zbx_api import Apis

def getAlert():
    apis = Apis("10.127.2.49","admin","zabbix")
    res = apis.get_alerts("host-3","1507564800","1507623810")
    return res

def writeAlertIntoXml(alertInfo=""):
    #create workbook and sheet
    workbook = xlwt.Workbook()
    AlertInformation = workbook.add_sheet("AlertInformation", cell_overwrite_ok=True)
    
    #add Xtitle
    row0 = ["TRIGGER_NAME","HOST_NAME","TRIGGER_STATUS","TRIGGER_SEVERITY"]
    for i in xrange(len(row0)):
        AlertInformation.write(0,i,row0[i])
    
    #add alert information
    
    
    #save
    workbook.save("alertInformation.xlsx")
    
def main():
    response = getAlert()
    
    alertRes = response['result']
    print alertRes
#     writeAlertIntoXml()
    
if __name__ == "__main__":
    main()

