#!/usr/bin/env python
#-*- conding: utf8 -*-

import json
import pika
from optparse import OptionParser

opt_parser = OptionParser()
opt_parser.add_option("-r","--routing-key",dest="routing-key",help="Routing key for message (e.g.)")
opt_parser.add_option("-m",dest="message",help="Message text for alerts.")
args = opt_parser.parse_args()[0]

creds_broker = pika.PlainCredentials("alert_user","alertme")
conn_params = pika.ConnectionParameters("localhost",virtual_host="/",creds_broker)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

msg = json.dumps(args.message if args.message is not None else "critical.critical")
msg_props = pika.BasicProperties()
msg_props.content_type = "application/json"
msg_props.durable = False

channel.basic_pulish(body=msg,exchange="alerts",properties=msg_props,routing_key=args.routing_key)
print " [x] Sent %s" , str(msg)

conn_broker.close()