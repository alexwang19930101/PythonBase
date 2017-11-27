#！/usr/bin/env python
#-*- coding: utf8 -*-

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange='log',type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='log',routing_key='',body=message)
print " [x] Sent %r" % (message,)
connection.close()