#!/usr/bin/env python
#-*- coding: utf-8 -*-

# while True:
#     reply = raw_input('enter text:')
#     if reply == 'stop': break
#     print(reply)

while True:
    reply = raw_input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('bad!'*2)
    else:
        num = int(reply)
        print num**2
print('bye')