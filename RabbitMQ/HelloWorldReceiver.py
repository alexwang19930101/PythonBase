#!/usr/bin/env python  
import pika

#连接到RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  
#获取信道
channel = connection.channel()
#声明交换机、队列——declare的意识是如果没有就创建，否则就继续
#此处并没有声明交换机、使用默认交换机？
channel.queue_declare(queue='hello')
  
print ' [*] Waiting for messages. To exit press CTRL+C'
#定义处理消息回调的函数
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
#订阅队列
channel.basic_consume(callback,queue='hello',no_ack=True)
#开始消费：这是一个阻塞的循环等待，若要让它停止可在回调函数中分支结构处理
channel.start_consuming()