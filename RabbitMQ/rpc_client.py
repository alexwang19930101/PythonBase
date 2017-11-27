#!/usr/bin/env python
import pika
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        self.connnection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connnection.channel()
        
        result = self.connnection.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        
        self.channel.basic_consume(self.on_respense,no_ack=True,queue=self.callback_queue)
        
    def on_respense(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body
    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_pulish(exchange='rpc_queue',properties=pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.corr_id),body=str(n))
        while self.response is None:
            self.connnection.process_data_events()
        return int(self.response)
    
fibonacci_rpc = FibonacciRpcClient()

print " [x] Requesting fib(30)"
response = fibonacci_rpc.call(30)
print " [.] Got %r" % (response,)