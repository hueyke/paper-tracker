#!/usr/bin/env python
from __future__ import print_function
import smtplib
from email.mime.text import MIMEText

def send(status):
    gmail_user = 'hueyke@gmail.com'
    gmail_password = 'rmqwaiecdtppcosm'
    
    msg = MIMEText('Hi Huey,\n\nScience status changed to \"%s\".\n\nBest,\nHuey' % status)
    msg['Subject'] = 'Science status changed to \"%s\"!' % status
    msg['From'] = gmail_user
    msg['To'] = gmail_user
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, [gmail_user], msg.as_string())
        server.close()
    
        print('Email sent!')
        return True
    except:
        print('Something went wrong...')
        return False


if __name__ == '__main__':
    send('test')
