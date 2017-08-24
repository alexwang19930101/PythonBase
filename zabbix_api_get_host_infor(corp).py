#!/usr/bin/env python
#-*- coding:utf8 -*-

import os, sys
import glob
import json
import urllib2
from urllib2 import URLError

class Client:
        def __init__(self,host="127.0.0.1",user="admin",password="zabbix",vip=""):
                self.host = host
                self.vip = vip
                self.auth = ""
                self.url = "http://%s/zabbix/api_jsonrpc.php" % host
                self.id = 0
                #get self.auth by login()
                self.login(user,password)

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

                result = self.doRequest(data)

                if "result" not in result:
                        print "ERROR %s Message %s" % (result["error"]["data"],result["error"]["message"])
                        return []
                else:
                        return result["result"]

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
def main():
    client = Client("192.168.101.134:10080","admin","zabbix","")
    print client.auth
    
if __name__ == "__main__":
    main()