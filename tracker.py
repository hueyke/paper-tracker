#!/usr/bin/env python
import grl as journal
import gmail
import time

def track(previousStatus):
    status = journal.getArticleStatus()
    if status != previousStatus:
        gmail.send(journal.getName(), status)
    return status

def run():
    previousStatus = ''
    while True:
        status = track(previousStatus)
        print('[%s] %s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), status))
        previousStatus = status
        time.sleep(30)
if __name__ == '__main__':
    run()
