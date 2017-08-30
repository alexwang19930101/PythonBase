from socket import *

myhost="127.0.0.1"
myport=8080

socketobj = socket(AF_INET,SOCK_STREAM)

socketobj.connect((myhost,myport))
print socketobj.recv(1024)

for data in ['a','b','c']:
    socketobj.send(data)
    print socketobj.recv(1024)
socketobj.send('exit')
socketobj.close()