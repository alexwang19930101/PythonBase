#!/usr/bin/env python
#-*- coding:utf-8 -*-

from zbx_api import Apis

def main():
    apis = Apis("10.127.2.49","admin","zabbix")
    res = apis.get_alerts("host-3","1507564800","1507623810")
    print res
if __name__ == "__main__":
    main()

