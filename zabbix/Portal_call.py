#!/usr/bin/env python
#-*- coding: utf8 -*-

import zbx_api
import json
from threading import Thread

class Portal_call():
    def __init__(self,zbx_vip="10.127.2.49",user="admin",pwd="zabbix"):
        self.zbx_apis = zbx_api.Apis(zbx_vip,user,pwd)

    def bubble_sort(self,data,key,num):
        for i in range(num):
            for j in range(len(data)-1-i):
                if (data[j][key] > data[j + 1][key]):
                    data[j],data[j+1] = data[j+1],data[j]
        return data
    
    def get_itemtop(self,num,item):
        res_infor = self.zbx_apis.get_item(item)["result"]
        res_hostinfor = self.zbx_apis.get_hostname()["result"]
        if num > len(res_infor):
            num = len(res_infor)
            
        res_infor_sorted = self.bubble_sort(res_infor,"lastvalue",num)[::-1]
        
        res_json_list = []
        for i in xrange(num):
            for j in xrange(len(res_hostinfor)):
                if res_hostinfor[j]["hostid"] == res_infor_sorted[i]["hostid"]:
                    res_json_list.append({res_hostinfor[j]["host"]:res_infor_sorted[i]["lastvalue"]})
                    break
        return res_json_list

    def get_cpuTop(self,num):
        return self.get_itemtop(num,"system.cpu.load[percpu,avg1]")

    def get_memTop(self,num):
        return self.get_itemtop(num,"LSD_mempUsed")
    
    def get_host_state(self):
        host_infor =  self.zbx_apis.get_hostid()
        host_num = len(host_infor.keys())
        host_abnormal = 0
        host_poweroff = 0
        for i in host_infor.keys():
            if host_infor[i][1] != "":
                host_abnormal += 1
            if "off" in self.zbx_apis.get_scriptRES(i):
                host_poweroff += 1
        host_abnormal = host_abnormal - host_poweroff
        hostnormal = host_num - host_abnormal - host_poweroff
        
        res_key = ['normal','abnormal','poweroff']
        res_value = [hostnormal,host_abnormal,host_poweroff]
        res_json = json.dumps(dict(zip(res_key,res_value)))
        return res_json
    
    def get_host_health(self):
        health_scores = {}
        host_infor =  self.zbx_apis.get_hostid()
        
        def get_host_score(hostid):
            hostname = host_infor[hostid][0]
            score = self.zbx_apis.get_host_trigger(hostid)
            health_scores[hostname] = score
        
        threads = []
        for hostid in host_infor.keys():
            t = Thread(target=get_host_score, args=[hostid])
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
        
        return health_scores

    
    def get_trigger(self):
        return self.zbx_apis.get_trigger()

def main():
    import time
    portal_call = Portal_call()
    time_start = time.time()
    res = portal_call.get_host_health()
#     res1 = portal_call.get_trigger()
#     res2 = portal_call.get_memTop(50000)
#     res3 = portal_call.get_cpuTop(5)
    time_end = time.time()
    print res
    print time_end-time_start
        
if __name__ == "__main__":
    main()