#!/usr/bin/env python
#-*- conding: utf8 -*-

import json,smtplib
import pika

def send_email(recipients,subject,message):
#     """E-mail generator for received alerts"""
#     headers = ("From: %s\r\nTo: \r\nData: \r\nSubject: %s\r\n\r\n") % ("igis_wxy@fiberhome.com",subject)
#     smtp_server = smtplib.SMTP()
#     smtp_server.connenct("mail.fiberhome.com",25)
#     smtp_server.sendmail("igis_wxy@fiberhome.com", recipients, headers + str(message))
#     smtp_server.close()
    print("From: %s\r\nTo: \r\nData: \r\nSubject: %s\r\n\r\n") % ("igis_wxy@fiberhome.com",subject)

def critical_notify(channel,method,header,body):
    """"sends critical alerts to administrators via e-mail"""
    EMAIL_RECIPS = ["77034519@qq.com",]
    
    message = json.loads(body)
    
    send_email(EMAIL_RECIPS, "CRITICAL ALERTS", message)
    print "Sent alert via e-mail!Alert Text: %s\r\nRecipients: %s" % (str(message),str(EMAIL_RECIPS))
    
    channel.basic_ack(delivery_tag=method.delivery_tag)

def rate_limit_notify(channel,method,header,body):
    """"sends rate limit message to administrators via e-mail"""
    
    """"sends critical alerts to administrators via e-mail"""
    EMAIL_RECIPS = ["77034519@qq.com",]
    
    message = json.loads(body)
    
    send_email(EMAIL_RECIPS, "RATE LIMIT ALERTS", message)
    print "Sent alert via e-mail!Alert Text: %s\r\nRecipients: %s" % (str(message),str(EMAIL_RECIPS))
    
    channel.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    AMQP_SERVER = "localhost"
    AMQP_USER = "alert_user"
    AMQP_PASS = "alertme"
    AMQP_VHOST = "/"
    AMQP_EXCHANGE = "alerts"
    
    creds_broker = pika.PlainCredentials(AMQP_USER,AMQP_PASS)
    conn_params = pika.ConnectionParameters(AMQP_SERVER,virtual_host=AMQP_VHOST,credential = creds_broker)
    conn_broker = pika.BlockingConnection(conn_params)
    channel = conn_broker.channel()

    channel.exchange_declare(exchange=AMQP_EXCHANGE,type="topic",auto_delete=False)
    
    channel.queue_declare(queue="critical",auto_delete=False)
    channel.queue_bind(queue="critical",exchange=AMQP_EXCHANGE,routing_key="critical.*")
    channel.queue_declare(queue="rate_limit",auto_delete=False)
    channel.queue_bind(queue="rate_limit",exchange=AMQP_EXCHANGE,routing_key="*.rate_limit")

    channel.basic_consume(critical_notify,queue="critical",no_ack=False,consumer_tag="critical")
    channel.basic_consume(rate_limit_notify,queue="rate_limit",no_ack=False,consumer_tag="rate_limit")
    
    print "Ready for alerts"
    channel.start_consuming()