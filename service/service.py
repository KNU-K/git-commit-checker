#!/usr/bin/env python3
# Anchor extraction from HTML document

import datetime
import configparser
from modules import crawler,mail,json_rw


def run():
    config = configparser.ConfigParser()
    config.read('config/smtp.ini')
    now = datetime.datetime.now()
    smtp_config = {
        'smtp_server' : config.get('smtp', 'smtp_server'),
        'smtp_port' : config.get('smtp', 'smtp_port'),
        'smtp_email' : config.get('smtp', 'smtp_email'),
        'smtp_password' : config.get('smtp', 'smtp_password')
    }
    json_config = {
        'user' : './json/user.json'
    }

    jsonRW = json_rw.JsonRW(json_config)
    mailService = mail.Mail(smtp_config)
    
    # get user information
    users = jsonRW.read('user')
    for user in users:
        isCrawling = crawler.Crawler.run(user['userid'], now.strftime('%Y-%m-%d'))
        if int(isCrawling) == 0:
            mailService.send(user['email'])
            print('GOod')

