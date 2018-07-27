import science
import gmail
import time
from datetime import datetime


def track(previousStatus):
    status = science.getArticleStatus()
    if status != previousStatus:
        gmail.send(status)
    return status

def run():
    previousStatus = 'Under Evaluation'
    while True:
        status = track(previousStatus)
        print('[%s] %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), status))
        previousStatus = status
        time.sleep(600)
if __name__ == '__main__':
    run()
