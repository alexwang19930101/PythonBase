#!/usr/bin/env python 
#-*- coding:utf8 -*-

#导入模块，urllib2用来模拟浏览器的HTTP方法模块
import json
import urllib2
import sys
from urllib2 import URLError

#url and url header
zabbix_url = "http://192.168.101.134:8000/zabbix/api_jsonrpc.php"
zabbix_header = {"Content_Type":"application/json"}
zabbix_user = "admin"
zabbix_pass = "zabbix"
auth_code = ""

#auth user and password
#用户认证，获取一个SESSIONID
#生成用户名与密码

auth_data = json.dumps(
    {
        "jsonrpc":"2.0",
        "method":"user.login",
        "params":{
                "user":zabbix_user,
                "password":zabbix_pass
            },
        "id":0
    })

#create request object
request = urllib2.Request(zabbix_url,auth_data)
for key in zabbix_header:
    request.add_header(key, zabbix_header[key])
    
#get host list
try:
    result = urllib2.urlopen(request)
except URLError as e:
    if hasattr(e, 'reason'):
        print 'url error'
        print 'Reason',e.reason
    elif hasattr(e, 'code'):
        print 'url error'
        print 'Error code:',e.code
else:
    response = json.loads(result.read())
    result.close()

print response
print "type of hosts:",type(response)
