#!/usr/bin/env python
# encapsulation for zabbix api
import json
import urllib2
import sys
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
    
    def get_hostid(self,hostname):
        auth = self.user_login()
        params = {"output" : ["hostid", "host"], "selectInterfaces" : ["interfaceid", "ip"]}
        data = {"jsonrpc" : self.jsonrpc,"method" : "host.get","params" : params,"id" : "2","auth" : auth}
        res_json = self.do_request(data)
#        print(res_json)
#        hostname = socket.gethostname()
#        hostname = "host-5"
        lens = len(res_json["result"])
        for i in xrange(lens):
            if res_json["result"][i]["host"] == hostname:
                return res_json["result"][i]["hostid"]
            else:
                continue
    def ipmi_init(self,ipmi_passwd,hostname=""):
        auth = self.user_login()
        hostid = self.get_hostid(hostname)
        params = {"hostid": hostid,"ipmi_authtype": -1,"ipmi_privilege": 4,"ipmi_username": "root","ipmi_password": ipmi_passwd}
        data = {"jsonrpc" : self.jsonrpc,"method" : "host.update","params" : params,"id" : "3","auth" : auth}
        res_json = self.do_request(data)
#        print(res_json)

    def ipmi_addif(self,ipmi_ip,hostname=""):
        auth = self.user_login()
        hostid = self.get_hostid(hostname)
        params = {"hostid": hostid,"dns": "","ip": ipmi_ip,"main": 1,"port": "623","type": 3,"useip": 1}
        data = {"jsonrpc" : self.jsonrpc,"method" : "hostinterface.create","params" : params,"id" : "4","auth" : auth} 
        res_json = self.do_request(data)
        print(res_json)

    def snmp_addif(self,hostname=""):
        auth = self.user_login()
        hostid = self.get_hostid(hostname)
        params = {"hostid": hostid,"dns": "","ip": "127.0.0.1","main": 1,"port": "161","type": 2,"useip": 1}
        data = {"jsonrpc" : self.jsonrpc,"method" : "hostinterface.create","params" : params,"id" : "5","auth" : auth}
        res_json = self.do_request(data)
             
    def get_alerts(self,hostname,time_from,time_to):
        auth = self.user_login()
        hostid = self.get_hostid(hostname)
        #params = {"output": "extend","actionids": "84","hostids": hostid,"time_from": time_from,"time_till": time_to}
        params = {"output": "extend","actionids": "84","hostids": hostid}
        data = {"jsonrpc" : self.jsonrpc,"method" : "alert.get","params" : params,"id" : "6","auth" : auth}
        res_json = self.do_request(data)
        return res_json
#    def get_alerts(self,time_from,time_to):

