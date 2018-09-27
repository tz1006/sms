#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename: send.py
# description: sms 发送
#    - login()
#    - check_last_login()
#    - text
#    - text
# parameters: 
#    - text
#    - text
#    - text
#    - text
#    - phone
#    - 
#    - 
# useage: 
        



import nexmo
improt time

api_key = 'd1258708'
api_secret = 'Nosecret'



def login():
    global client
    global last_login_time
    message = '  api_key: {0} \n  api_secret: {1}'.format(api_key, api_secret)
    print('正在登陆...')
    print(message)
    client = nexmo.Client(key=api_key, secret=api_secret)
    last_login_time = time.time()


def check_last_login(alive=290):
    now_time = time.time()
    time_past = int(now_time - last_login_time)
    if time_past < alive:
        message = '上次登录%d秒前，无需登录' % time_past
        print(message)
    else:
        message = '上次登录%d秒前，重新登录' % time_past
        print(message)
        login()


def send(message):
    check_last_login()
    
    
    
        
        
class send:
    def __init__ ():
        init()
    def init():
    
