#!/usr/bin/env python
#-*- coding:utf8 -*-

import os, sys
import glob
import json
import urllib2
from urllib2 import URLError
import time,datetime

class Client:
	def __init__(self,host="127.0.0.1",user="admin",password="zabbix",vip=""):
            self.host = host
            self.vip = vip
            self.auth = ""
            self.url = "http://%s/zabbix/api_jsonrpc.php" % host
            #print self.url
            self.id = 0
            #get self.auth by login()
            self.auth = self.login(user,password)

	def callAPI(self,method,params={},auth_bool=True):
            data={
            	"jsonrpc": "2.0",
            	"method": method,
            	"params": params,
            	"auth": self.auth,
            	"id": self.id
            }
            
            if not auth_bool:
            	del data['auth']
            
            res = self.doRequest(data)
            
            if 'result' not in res:			
            	print "ERROR: %s msg:%s" % (res['error']['data'],res['error']['message'])
            	return []
            
            return res["result"]
            
	def doRequest(self,data):
            header = {"Content-Type":"application/json"}
            data = json.dumps(data)
            request = urllib2.Request(self.url,data)
            for key in header:
            	request.add_header(key,header[key])	
            
            try:
            	result = urllib2.urlopen(request)
            except URLError as e:
            	if hasattr(e,"code"):
            		print "error code:%s" % e.code
            	elif hasattr(e,"reason"):
            		print "error reason:%s" % e.reason
            else:
                response = json.loads(result.read())
	        result.close()
	    return response
	
	def login(self,user="admin",password="zabbix"):
            params = {
            	"user":user,
            	"password":password
            }
            self.auth = self.callAPI(params=params,method="user.login",auth_bool = False)
            return self.auth

        def getAlert(self,offset=10):
            datetime_now = datetime.datetime.now()
            timetuple_now = datetime_now.timetuple()
            timestamp_now = time.mktime(timetuple_now)
            timestamp_offset = timestamp_now - offset*60

            alertParams = {
                "output": "extend",
                "time_from": timestamp_offset,
                "time_till": timestamp_now
            } 
            self.id = 2
            alertGetRes = self.callAPI(method="alert.get",params=alertParams,auth_bool = True)
            return alertGetRes

def main():
	serverHost = "%s:%s" % ("192.168.101.134","10080")
	client = Client(serverHost,"admin","zabbix","")
	print client.auth
	alertGetRes = client.getAlert()
	print alertGetRes

if __name__ == "__main__":
	main()

