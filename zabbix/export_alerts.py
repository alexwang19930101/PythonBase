import argparse
import zbx_api
import xlwt
import datetime

class ArgParse():
    
    def __init__(self):
        parser = argparse.ArgumentParser()
        
        parser.add_argument('-user',default='admin',dest='user',help='zabbix username')
        parser.add_argument('-passwd',default='zabbix',dest='passwd',help='zabbix password')
        parser.add_argument('-addr',default='127.0.0.1',dest='addr',help='zabbix vip')
        parser.add_argument('-module',default='list',dest='module',help='module')
        parser.add_argument('-host',default='',dest='host',help='hostname')
        parser.add_argument('-from',default='',dest='t_from',help='time from')
        parser.add_argument('-to',default='',dest='t_to',help='time to')

        self.args = parser.parse_args()

    # turn result into excel format
    def export_to_excel(self,res):
        #create workbook and sheet
        workbook = xlwt.Workbook()
        AlertInforSheet = workbook.add_sheet("AlertInforSheet", cell_overwrite_ok=True)
        
        #add Xtitle
        row0 = ["TRIGGER_NAME","HOST_NAME","TRIGGER_STATUS","TRIGGER_SEVERITY","TRIGGER_TIME"]
        for i in xrange(len(row0)):
            AlertInforSheet.write(0,i,row0[i])
        
        #add alert information
        alertResList = res['result']
    
        for i in xrange(len(alertResList)):
            messagelist = alertResList[i]['message'].split('*')
            for j in xrange(len(messagelist)):
                AlertInforSheet.write(i+1,j,messagelist[j])
            #add Trigger_TIME
            triggerTimeStamp = alertResList[i]['clock']
            triggerTimeStr = datetime.datetime.fromtimestamp(float(triggerTimeStamp)).strftime("%Y-%m-%d %H:%M:%S")
            AlertInforSheet.write(i+1,4,triggerTimeStr)
            
        #save
        workbook.save("alertInformation_%s.xlsx" % datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
        
class GetAlerts():
    
    def __init__(self):
        self.args = ArgParse().args    
    
    def get_alert_list(self):
        addr = self.args.addr
        username = self.args.user
        password = self.args.passwd
        apis = zbx_api.Apis(addr,username,password)

        hostname = self.args.host
        time_from = self.args.t_from
        time_to = self.args.t_to
        if hostname == '':
            return 0

        res = apis.get_alerts_list(hostname,time_from,time_to)
        return res

    def get_alert_report(self):
        addr = self.args.addr
        username = self.args.user
        password = self.args.passwd
        apis = zbx_api.Apis(addr,username,password)

        time_from = self.args.t_from
        time_to = self.args.t_to

        res = apis.get_alerts_report(time_from,time_to)
        return res

if __name__ == "__main__":
    calerts = GetAlerts()
    res = calerts.get_alert_report()
    ArgParse().export_to_excel(res)
