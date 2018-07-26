import science
import gmail
import time

def track(previousStatus):
    status = science.getArticleStatus()
    if status != previousStatus:
        gmail.send(status)
    return status

def run():
    previousStatus = 'Under Evaluation'
    while True:
        status = track(previousStatus)
        print('[%s] %s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), status))
        previousStatus = status
        time.sleep(600)
if __name__ == '__main__':
    run()
