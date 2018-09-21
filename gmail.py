#!/usr/bin/env python
from __future__ import print_function
from email.mime.text import MIMEText
import smtplib
import auth


def send(journal, status):
    gmail_user = auth.getGmailAddress()
    gmail_password = auth.getGmailPassword()
    
    msg = MIMEText('Hi Huey,\n\n%s status changed to \"%s\".\n\nBest,\nHuey' % (journal, status))
    msg['Subject'] = '%s status changed to \"%s\"!' % (journal, status)
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
