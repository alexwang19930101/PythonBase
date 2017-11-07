#!/usr/bin/env python
# encapsulation for zabbix api
import json
import urllib2
import socket


#ZABBIX_VIP=sys.argv[1] if sys.argv[1] else "127.0.0.1"
#ZABBIX_USERNAME=sys.argv[2] if sys.argv[2] else "admin"
#ZABBIX_PASSWORD=sys.argv[3] if sys.argv[3] else "zabbix"

class Apis():
    def __init__(self,zbx_ip,username,passwd,jsonrpc="2.0"):
        self.jsonrpc = jsonrpc
        self.zbx_ip = zbx_ip
        self.url = "http://%s:10080/zabbix/api_jsonrpc.php" %(zbx_ip)
        self.username = username
        self.passwd = passwd
        self.auth = self.user_login()

    def do_request(self,data):
        header = {"Content-Type": "application/json"}
        data = json.dumps(data)
        request = urllib2.Request(self.url,data)
        for key in header:
            request.add_header(key,header[key])
        res = urllib2.urlopen(request)
        if res.code != 200:
            print("ERROR:HTTP status :%s" %(res.code))
        res_json = json.loads(res.read())
        
        return res_json

    def user_login(self):
        params = {"user":self.username,"password":self.passwd}
        data = {"jsonrpc":self.jsonrpc,"method":"user.login","params":params,"id":"1"}
        res_json = self.do_request(data)
        
        return res_json["result"]

    def get_hostname(self):
        params = {"output" : ["hostid", "host"]}
        data = {"jsonrpc" : self.jsonrpc,"method" : "host.get","params" : params,"id" : "2","auth" : self.auth}
        res_json = self.do_request(data)
        
        return res_json
    
    def get_hostname_id(self,hostid):
        params = {"output" : ["hostid", "host"], "selectInterfaces" : ["interfaceid", "ip"]}
        data = {"jsonrpc" : self.jsonrpc,"method" : "host.get","params" : params,"id" : "3","auth" : self.auth}
        res_json = self.do_request(data)
        lens = len(res_json["result"])
        for i in xrange(lens):
            if res_json["result"][i]["hostid"] == hostid:
                return res_json["result"][i]["host"]
    
    def get_hostid(self):
        params = {"output" : ["hostid", "host","error"]}
        data = {"jsonrpc" : self.jsonrpc,"method" : "host.get","params" : params,"id" : "4","auth" : self.auth}
        res_json = self.do_request(data)
        res_hostidList = []
        res_hostInfor = []
        lens = len(res_json["result"])
        for i in xrange(lens):
            res_hostidList.append(res_json["result"][i]["hostid"])
            res_hostInfor.append((res_json["result"][i]["host"],res_json["result"][i]["error"]))           
        return dict(zip(res_hostidList,res_hostInfor))
    
    def get_host_trigger(self,hostid):
        params = {"output": ["triggerid","description","priority"],"filter": {"value": 1,"hostid" : hostid},"sortfield": "priority","sortorder": "DESC"}
        data = {"jsonrpc" : self.jsonrpc,"method" : "trigger.get","params" : params,"id" : "5","auth" : self.auth}
        res_json = self.do_request(data)
        trigger_levelnum = [0,0,0,0]
        for i in xrange(len(res_json['result'])):
            if res_json['result'][i]['priority'] in ['0','1']:
                trigger_levelnum[0] += 1
                continue
            elif res_json['result'][i]['priority'] in ['2','3']:
                trigger_levelnum[1] += 1
                continue
            elif res_json['result'][i]['priority'] == '4':
                trigger_levelnum[2] += 1
                continue
            else:
                trigger_levelnum[3] += 1
        trigger_levelnum[0] = trigger_levelnum[0] * 0.5
        trigger_levelnum[1] = trigger_levelnum[1] * 1.0
        trigger_levelnum[2] = trigger_levelnum[2] * 2.0
        trigger_levelnum[3] = trigger_levelnum[3] * 3.0
        score = 100.0 - trigger_levelnum[0] - trigger_levelnum[1] - trigger_levelnum[2] - trigger_levelnum[3]
        if score < 60:
            return 60
        return score

    def get_trigger(self):
        params = {"output": ["triggerid","description","priority"],"filter": {"value": 1},"sortfield": "priority","sortorder": "DESC"}
        data = {"jsonrpc" : self.jsonrpc,"method" : "trigger.get","params" : params,"id" : "6","auth" : self.auth}
        res_json = self.do_request(data)
        print res_json
        trigger_level = ['information','warning','serious','disaster']
        trigger_levelnum = [0,0,0,0]
        for i in xrange(len(res_json['result'])):
            if res_json['result'][i]['priority'] in ['0','1']:
                trigger_levelnum[0] += 1
                continue
            elif res_json['result'][i]['priority'] in ['2','3']:
                trigger_levelnum[1] += 1
                continue
            elif res_json['result'][i]['priority'] == '4':
                trigger_levelnum[2] += 1
                continue
            else:
                trigger_levelnum[3] += 1
        trigger_inforDict = dict(zip(trigger_level,trigger_levelnum))
        
        return trigger_inforDict

    def get_item(self,key):
        params = {"output": ["itemid","hostid","key_","lastvalue"],"filter": {"key_": key}}
        data = {"jsonrpc" : self.jsonrpc,"method" : "item.get","params" : params,"id" : "7","auth" : self.auth}
        res_json = self.do_request(data)
          
        return res_json
    
    def get_scriptID(self):
        params = {"output": "extend"}
        data = {"jsonrpc" : self.jsonrpc,"method" : "script.get","params" : params,"id" : "8","auth" : self.auth}
        res_json = self.do_request(data)
        for i in xrange(len(res_json['result'])):
            res = res_json['result'][i]['command']
            if "status" in res:
                return res_json['result'][i]['scriptid']
                break
            continue

    def get_scriptRES(self,hostid):
        scriptid = self.get_scriptID()
        params = {"scriptid": scriptid,"hostid":hostid}
        data = {"jsonrpc" : self.jsonrpc,"method" : "script.execute","params" : params,"id" : "9","auth" : self.auth}
        res_json = self.do_request(data)
        return res_json

