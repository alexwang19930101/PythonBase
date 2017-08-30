#-*- coding:utf8 -*-
from socket import *
import threading
import time
import traceback

myhost=''
myport=8080

socketObj = socket(AF_INET,SOCK_STREAM)
socketObj.bind((myhost,myport))
socketObj.listen(5)
print 'waiting for connection'

def tcplink(sock,address):
    print 'accept connection from %s:%s'%address
    sock.send("welcome")
    while True:
        try:
            data = sock.recv(1024).strip()
            time.sleep(1)
            if data == "exit" or not data:
                break
            sock.send('Hello,%s' % data)
        except:
            traceback.print_exc()
            break
    sock.close()
    print "connection from %s:%s closed" % address
    
while True:
    sock,address = socketObj.accept()
    t = threading.Thread(target=tcplink(sock, address))
    t.start()