#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename: send.py
# description: 等待，时间控制

import nexmo

api_key = 'd1258708'
api_secret = 'Nosecret'

def init():
    global client
    message = '  api_key: {0} \n  api_secret: {1}'.format(api_key, api_secret)
    print('正在登陆...')
    print(message)
    client = nexmo.Client(key=api_key, secret=api_secret)




class send:
    def __init__ ():
        init()
    def init():
    
