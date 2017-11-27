#!/usr/bin/env python
import pika
import sys
#连接到RabbitMQ，默认运行在5672端口
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#获取信道
channel = connection.channel()
#声明交换器、队列
channel.queue_declare(queue='hello')
#创建消息、发布消息
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',routing_key='hello',body=message)

print " [x] Sent 'Hello World!'"
#关闭信道、关闭连接
connection.close()